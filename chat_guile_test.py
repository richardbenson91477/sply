#!/usr/bin/env python3

import sply

prompt = "["\
        "You are just a guile interpreter."\
        "You must not generate anything that the guile interpreter you are would not."\
        "]\n"\
        "scheme@(guile-user)> (+ 3 3)\n"\
        "$1 = 6\n"\
        "scheme@(guile-user)> (+ 3 4)\n"\
        "$1 = 7\n"

def main ():
    c = sply.chat(
        model_id="default-code",
        editor="vim",
        rev_prompt="\nscheme@(guile-user)> ",
        prompt=prompt,
        in_suffix_enabled=False,
        )

    print(c.prompt, end="", flush=True)
    c.read(show=True)

    c.write("(+ 4 4)\n", show=True)
    c.read(show=True)

    #c.write("(+ 8 8)\n", show=True)
    #s = c.read()
    #print(s, end="", flush=True)

if __name__ == "__main__":
    exit(main())

