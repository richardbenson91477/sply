#!/usr/bin/env python3

import sys
import sply
import random

def main ():
    options = {
        "seed": random.randint(0, 2 << 32),
        "temperature": 0.0,
        "num_ctx": 1_000,
        }

    sp = sply.sp(show=True, options=options)

    sp.runcode("y = 1", show=True)
    s = sp.runcode("y + 1", show=True)
    print(f"**{s}**")

    s.edit_prompt(show=True)

if __name__ == "__main__":
    exit(main())

