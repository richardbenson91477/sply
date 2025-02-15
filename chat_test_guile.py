#!/usr/bin/env python3

import random
import sply

prompt = "["\
        "You are just a guile interpreter."\
        "You must not generate anything that the guile interpreter you are would not."\
        "]\n"\
        "scheme@(guile-user)> (+ 1 1)\n"\
        "$1 = 2\n"\
        "scheme@(guile-user)> (+ 2 1)\n"\
        "$1 = 3\n"

def main ():
    c = sply.chat(
        model_id="default-code",
        editor="vim",
        rev_prompt="\nscheme@(guile-user)> ",
        prompt=prompt,
        in_suffix_enabled=False,
        options = {
            "seed": random.randint(0, 2 << 32),
            "temperature": 0.0,
            "num_ctx": 1_000,
            }
        )

    print(c.prompt, end="", flush=True)
    c.read(show=True)

    c.write("(* 3 2)\n", show=True)
    c.read(show=True)

if __name__ == "__main__":
    exit(main())

