#!/usr/bin/env python3
"""Check technical product-Short output requirements using ffprobe.

This cannot determine whether audio contains female speech, whether a stream is
silent, or whether a product/story/caption is accurate. Watch and listen too.
"""

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys


def number(value):
    """Parse ffprobe numeric fields, treating unknown values as unavailable."""
    try:
        result = float(Fraction(str(value).replace(":", "/")))
    except (ValueError, ZeroDivisionError, TypeError):
        return None
    return result if math.isfinite(result) else None


def validate(metadata, *, preview=False, fps=30, duration=None, allow_silent=False):
    """Return technical errors without claiming to validate media content."""
    errors = []
    if allow_silent and not preview:
        errors.append("Silent output is allowed only for a disclosed preview.")
    if not isinstance(metadata, dict):
        return ["ffprobe output must be a JSON object."]

    streams = metadata.get("streams", [])
    if not isinstance(streams, list):
        return ["ffprobe did not provide a valid streams list."]
    streams = [stream for stream in streams if isinstance(stream, dict)]
    videos = [
        stream
        for stream in streams
        if stream.get("codec_type") == "video"
        and not (stream.get("disposition") or {}).get("attached_pic")
    ]
    audio = [stream for stream in streams if stream.get("codec_type") == "audio"]

    if not videos:
        errors.append("No video stream found.")
    else:
        video = videos[0]
        expected_size = (540, 960) if preview else (1080, 1920)
        actual_size = (video.get("width"), video.get("height"))
        if actual_size != expected_size:
            errors.append(
                f"Expected {expected_size[0]}x{expected_size[1]}, "
                f"got {actual_size[0]}x{actual_size[1]}."
            )
        actual_fps = number(video.get("avg_frame_rate"))
        if not actual_fps:
            actual_fps = number(video.get("r_frame_rate"))
        if actual_fps is None or abs(actual_fps - fps) > 0.01:
            errors.append(f"Expected {fps} fps, got {actual_fps}.")
        if video.get("codec_name") != "h264":
            errors.append(f"Expected H.264 video, got {video.get('codec_name')}.")
        if video.get("pix_fmt") != "yuv420p":
            errors.append(f"Expected yuv420p, got {video.get('pix_fmt')}.")
        if number(video.get("sample_aspect_ratio")) != 1:
            errors.append("Square pixels (sample_aspect_ratio 1:1) are required.")

        rotations = [(video.get("tags") or {}).get("rotate", 0)]
        rotations.extend(
            side.get("rotation", 0)
            for side in (video.get("side_data_list") or [])
            if isinstance(side, dict)
        )
        if any(
            number(rotation) is None or abs(number(rotation) % 360) > 0.001
            for rotation in rotations
        ):
            errors.append("Bake rotation into the pixels; rotation metadata must be zero.")

    if not audio and not allow_silent:
        errors.append("Required audio stream is missing; female narration is not verified.")
    for index, track in enumerate(audio, start=1):
        if track.get("codec_name") != "aac":
            errors.append(f"Audio track {index} must be AAC, got {track.get('codec_name')}.")

    container = metadata.get("format") or {}
    if not isinstance(container, dict):
        container = {}
    formats = str(container.get("format_name", "")).split(",")
    if "mp4" not in formats:
        errors.append("Expected an MP4-compatible container reported by ffprobe.")

    actual_duration = number(container.get("duration"))
    if actual_duration is None and videos:
        actual_duration = number(videos[0].get("duration"))
    if actual_duration is None or actual_duration <= 0:
        errors.append("A positive video duration could not be verified.")
    else:
        if actual_duration > 180:
            errors.append(f"Duration {actual_duration:.3f}s exceeds the configured 180s Shorts limit.")
        if duration is not None:
            tolerance = max(0.1, 2 / fps)
            if abs(actual_duration - duration) > tolerance:
                errors.append(
                    f"Expected {duration:.3f}s (+/-{tolerance:.3f}s), "
                    f"got {actual_duration:.3f}s."
                )
    return errors


def positive_number(value):
    result = number(value)
    if result is None or result <= 0:
        raise argparse.ArgumentTypeError("must be a positive finite number")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path, help="Rendered MP4 to inspect")
    parser.add_argument("--preview", action="store_true", help="Expect 540x960 instead of 1080x1920")
    parser.add_argument("--fps", type=positive_number, default=30, help="Expected frame rate (default 30)")
    parser.add_argument("--duration", type=positive_number, help="Expected duration in seconds")
    parser.add_argument("--allow-silent", action="store_true", help="Allow missing audio for a disclosed preview only")
    args = parser.parse_args(argv)
    if args.allow_silent and not args.preview:
        parser.error("--allow-silent can be used only with --preview")
    if not args.video.is_file():
        parser.error(f"video file does not exist: {args.video}")
    ffprobe = shutil.which("ffprobe")
    if ffprobe is None:
        print("Check not run: ffprobe is not available on PATH.", file=sys.stderr)
        return 2

    try:
        result = subprocess.run(
            [
                ffprobe, "-v", "error", "-show_streams", "-show_format",
                "-of", "json", str(args.video.resolve()),
            ],
            capture_output=True,
            text=True,
            check=True,
            timeout=60,
        )
        metadata = json.loads(result.stdout)
    except subprocess.CalledProcessError as error:
        print(f"ffprobe failed: {error.stderr.strip()}", file=sys.stderr)
        return 2
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError) as error:
        print(f"Check not completed: {error}", file=sys.stderr)
        return 2

    errors = validate(
        metadata,
        preview=args.preview,
        fps=args.fps,
        duration=args.duration,
        allow_silent=args.allow_silent,
    )
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: technical media checks. Still review the actual visuals, speech, and captions.")
    if args.allow_silent:
        print("This preview may be silent; required female narration remains pending.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
