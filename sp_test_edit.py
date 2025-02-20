#!/usr/bin/env python3

import sys
import random
import sply

def main ():
    model_id = "default-code"

    for argv in sys.argv[1:]:
        if argv.find("model_id=") == 0:
            model_id = argv[9:]

    seed = random.randint(0, 2 << 32)
    temp = 0.0
    num_ctx = 1_000

    sp = sply.sp(
        show=True,
        model_id=model_id,
        seed=seed,
        temp=temp,
        num_ctx=num_ctx,
        )

    sp.runcode("y = 1")
    s = sp.runcode("y + 1")
    print(f"**{s}**")

    sp.edit_prompt()
    return 0

if __name__ == "__main__":
    exit(main())

