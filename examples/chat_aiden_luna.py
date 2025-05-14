#!/usr/bin/env python3

import sys
import random
import sply

user_name1 = "Luna"
user_desc1 = "is a girl"
ai_name1 = "Aiden"
ai_desc1 = "is a boy"
port1 = 8080
in_suffix1 = f"{ai_name1}:"
rev_prompt1 = f"{user_name1}:"

user_name2 = ai_name1
user_desc2 = ai_desc1
ai_name2 = user_name1
ai_desc2 = user_desc1
port2 = port1 + 1
in_suffix2 = f"{ai_name2}:"
rev_prompt2 = f"{user_name2}:"

def main ():
    temp = 0.85
    num_ctx = 4_096

    seed1 = random.randrange(2**32)
    seed2 = random.randrange(2**32)
    print(f"seed1={seed1}; seed2={seed2}; ")

    c1 = sply.chat(
        backend="llama-server",
        port=port1,
        user_name=user_name1,
        user_desc=user_desc1,
        ai_name=ai_name1,
        ai_desc=ai_desc1,
        in_suffix=in_suffix1,
        rev_prompt=rev_prompt1,
        seed=seed1,
        temp=temp,
        num_ctx=num_ctx,
        )

    c2 = sply.chat(
        backend="llama-server",
        port=port2,
        user_name=user_name2,
        user_desc=user_desc2,
        ai_name=ai_name2,
        ai_desc=ai_desc2,
        in_suffix=in_suffix2,
        rev_prompt=rev_prompt2,
        seed=seed2,
        temp=temp,
        num_ctx=num_ctx,
        )

#    print(c.prompt, end="", flush=True)
    running = True
    while running:
        in1 = c1.read(show=True)
        c2.write(in1, show=True)
        in2 = c2.read(show=True)
        c1.write(in2, show=True)

    return 0


if __name__ == "__main__":
    exit(main())

