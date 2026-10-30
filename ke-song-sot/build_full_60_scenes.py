#!/usr/bin/env python3
"""Compatibility entry point for the explicitly edited version-3 film plan.

Edit PHAN_CANH_V3.json, then run this script; --check verifies without writing.
The pre-v3 source and prompts are preserved in revisions/before_v3_*.zip.
"""
from build_prompts_v3 import main

if __name__ == "__main__":
    main()
