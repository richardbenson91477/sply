#!/usr/bin/env python3

import sys
import random
import sply

from sp_examples import sp_example_conf


def main ():
    ex = sp_example_conf(
        mode="think",
        model_id="default-code", 
        seed = "",
        temp = 0.0,
        num_ctx = 1_000,
        show=True,
        )

    if not ex.parse_args(sys.argv):
        return -1

    sp = sply.sp(
        model_id=ex.model_id,
        seed=ex.seed,
        temp=ex.temp,
        num_ctx=ex.num_ctx,
        prompt=ex.prompt,
        show=ex.show,
        )

    if ex.mode == "plain":
        runcode = sp.runcode
    elif ex.mode == "think":
        runcode = sp.runcode_think

    runcode("i = 3 + 2")
    res = runcode("print(i ** 3)")
    print(f"**{res}**")
    res = runcode("print(i ** 3)")
    print(f"**{res}**")

    return 0


if __name__ == "__main__":
    exit(main())


