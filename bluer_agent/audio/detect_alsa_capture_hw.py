#!/usr/bin/env python3

import re
import subprocess
import sys
from typing import Optional


def detect_alsa_capture_hw() -> Optional[str]:
    """
    Detect first ALSA capture device and return hw:X,Y
    based on `arecord -l` output.
    """
    try:
        output = subprocess.check_output(
            ["arecord", "-l"],
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except Exception:
        return None

    # Example:
    # card 3: C930e [Logitech Webcam C930e], device 0: USB Audio [USB Audio]
    match = re.search(r"card\s+(\d+):.*device\s+(\d+):", output)
    if not match:
        return None

    card, device = match.groups()
    return f"hw:{card},{device}"


def main() -> int:
    hw = detect_alsa_capture_hw()
    if not hw:
        print("not-found", file=sys.stderr)
        return 1

    print(hw)
    return 0


if __name__ == "__main__":
    sys.exit(main())
