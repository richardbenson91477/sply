#!/usr/bin/env python3

import sys
import random
import sply


def main ():
    backend = ""
    model_id = ""
    for argv in sys.argv[1:]:
        if argv.find("backend=") == 0:
            backend = argv[8:]
        if argv.find("model_id=") == 0:
            model_id = argv[9:]

    sp = sply.sp(
        show=True,
        backend=backend,
        model_id=model_id,
        num_ctx=1_000,
        )

    sp.runcode("y = 1")
    s = sp.runcode("y + 1")
    print(f"**{s}**")

    sp.edit_prompt()
    return 0


if __name__ == "__main__":
    exit(main())


