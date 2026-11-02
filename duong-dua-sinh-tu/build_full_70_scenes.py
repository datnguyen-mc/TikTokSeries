#!/usr/bin/env python3
"""Compatibility wrapper that compiles PHAN_CANH_V3.json into all 70 scenes (420 clips)."""
import sys
from build_prompts_v3 import main

if __name__ == "__main__":
    main(sys.argv[1:])

