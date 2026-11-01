#!/usr/bin/env python3
"""Compatibility alias that calls build_prompts_v3.main()."""
import sys
from build_prompts_v3 import main

if __name__ == "__main__":
    main(sys.argv[1:])

