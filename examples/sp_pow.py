#!/usr/bin/env python3

import sys
import random
import sply


def main ():
    model_id = "default-code"
    seed = ""
    temp = 0.0
    num_ctx = 1_000

    for argv in sys.argv[1:]:
        if argv.find("model_id=") == 0:
            model_id = argv[9:]
        elif argv.find("seed=") == 0:
            seed = int(argv[5:])
        elif argv.find("temp=") == 0:
            temp = float(argv[5:])
        elif argv.find("num_ctx=") == 0:
            num_ctx = int(argv[8:])

    sp = sply.sp(
        show=True,
        model_id=model_id,
        num_ctx=num_ctx,
        temp=temp,
        seed=seed,
        )

    sp.runcode("y = 3 + 2")
    sp.runcode("print (y ** 3)")
    sp.runcode("print (pow (y, 3))")

    return 0


if __name__ == "__main__":
    exit(main())


