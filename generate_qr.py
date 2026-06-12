#!/usr/bin/env python3
"""Generate a QR code SVG for the published admissions page URL."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate admissions QR code.")
    parser.add_argument("url", help="Published admissions page URL, for example https://example.edu.cn/admissions/micro-major.html")
    parser.add_argument("-o", "--output", default="admissions-qr.svg", help="Output SVG path.")
    args = parser.parse_args()

    try:
      import qrcode
      import qrcode.image.svg
    except ModuleNotFoundError as exc:
      raise SystemExit(
          "Missing dependency: qrcode\n"
          "Install it in this project with: python3 -m pip install --target ./.deps qrcode\n"
          "Then run with: PYTHONPATH=./.deps python3 generate_qr.py <published-url>"
      ) from exc

    factory = qrcode.image.svg.SvgPathImage
    image = qrcode.make(args.url, image_factory=factory, border=2)
    output = Path(args.output)
    image.save(output)
    print(f"QR code saved to {output.resolve()}")


if __name__ == "__main__":
    main()
