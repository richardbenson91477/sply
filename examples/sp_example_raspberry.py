#!/usr/bin/env python3

import sys
import random
import sply

from sp_examples import sp_example_conf


def main ():
    ex = sp_example_conf(
        show=True,
        mode="think",
        num_ctx=1_000,
        )

    if not ex.parse_args(sys.argv):
        return -1

    sp = sply.sp(
        show=ex.show,
        backend=ex.backend,
        model_id=ex.model_id,
        seed=ex.seed,
        temp=ex.temp,
        num_ctx=ex.num_ctx,
        prompt=ex.prompt,
        )

    if ex.mode == "plain":
        runcode = sp.runcode
    elif ex.mode == "think":
        runcode = sp.runcode_think

    runcode("name = \"raspberry\"")

    res = runcode("print(name.count(\"r\"))")
    print(f"**{res}**")

    res = runcode("print(name.count(\"r\"))")
    print(f"**{res}**")

    return 0


if __name__ == "__main__":
    exit(main())


