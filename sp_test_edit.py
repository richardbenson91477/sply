#!/usr/bin/env python3

import sys
import random
import sply

def main ():
    model_id = "default-code"

    if len(sys.argv) > 1:
        for argv in sys.argv[1:]:
            if argv.find("model_id=") == 0:
                model_id = argv[9:]

    options = {
        "seed": random.randint(0, 2 << 32),
        "temperature": 0.0,
        "num_ctx": 1_000,
        }

    sp = sply.sp(show=True, model_id=model_id, options=options)

    sp.runcode("y = 1", show=True)
    s = sp.runcode("y + 1", show=True)
    print(f"**{s}**")

    sp.edit_prompt(show=True)

if __name__ == "__main__":
    exit(main())

