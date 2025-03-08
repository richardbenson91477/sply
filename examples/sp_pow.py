#!/usr/bin/env python3

import sys
import random
import sply


def main ():
    model_id = "default-code"

    for argv in sys.argv[1:]:
        if argv.find("model_id=") == 0:
            model_id = argv[9:]

    sp = sply.sp(model_id=model_id)

    sp.runcode("y = 3 + 2")
    s = sp.runcode("y ** 3")
    print(s)

    return 0

if __name__ == "__main__":
    exit(main())


