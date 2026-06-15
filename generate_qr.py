#!/usr/bin/env python3
"""Generate a QR code SVG for the published admissions page URL."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
DEPS_DIR = PROJECT_DIR / ".deps"
DEFAULT_URL = "https://zhaochengniu.github.io/weizhuanye/"

if DEPS_DIR.exists():
    sys.path.insert(0, str(DEPS_DIR))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate admissions QR code.")
    parser.add_argument(
        "url",
        nargs="?",
        default=DEFAULT_URL,
        help="Published admissions page URL.",
    )
    parser.add_argument("-o", "--output", default="admissions-qr.svg", help="Output SVG path.")
    args = parser.parse_args()

    try:
      import qrcode
      import qrcode.image.svg
    except ModuleNotFoundError as exc:
      raise SystemExit(
          "Missing dependency: qrcode\n"
          "Install it in this project with: /usr/bin/python3 -m pip install --target ./.deps qrcode\n"
          "Then run with: /usr/bin/python3 generate_qr.py"
      ) from exc

    factory = qrcode.image.svg.SvgPathImage
    image = qrcode.make(args.url, image_factory=factory, border=2)
    output = Path(args.output)
    image.save(str(output))
    print(f"QR code saved to {output.resolve()}")


if __name__ == "__main__":
    main()
