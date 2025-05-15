#!/usr/bin/env python3

import sys
import random
import sply

def main ():
    name_c1 = "Luna"
    name_c2 = "Aiden"

    c1_args = {
        "backend": "llama-server",
        "port": 8080,
        "user_name": name_c1,
        "user_desc": "is a girl",
        "ai_name": name_c2,
        "ai_desc": "is a boy I find very attractive",
        "in_suffix": f"{name_c2}:",
        "rev_prompt": f"{name_c1}:",
        "seed": random.randrange(2**32),
        "temp": 0.85,
        "num_ctx": 4_096,
        }
    print(f"c1_args={c1_args}")

    c2_args = {
        "backend": "llama-server",
        "port": 8081,
        "user_name": name_c2,
        "user_desc": "is a boy",
        "ai_name": name_c1,
        "ai_desc": "is a girl I find very unattractive",
        "in_suffix": f"{name_c1}:",
        "rev_prompt": f"{name_c2}:",
        "seed": random.randrange(2**32),
        "temp": 0.85,
        "num_ctx": 4_096,
        }
    print(f"c2_args={c2_args}")

    c1 = sply.chat(**c1_args)
    c2 = sply.chat(**c2_args)

    c2.prompt = c2.prompt[: c2.prompt.find('\n')] +\
          c2.make_prompt_greet(name_c1, name_c2)
    c2.updated_prompt()

    interactive = True
    running = True
    while running:
        in1 = c1.read(show=True)
        c2.write(in1, show=False)
        in2 = c2.read(show=True)
        c1.write(in2, show=False)
        while interactive and running:
            cmd = input('🔢')
            if not cmd:
                break
            elif cmd == '1':
                c1.edit_prompt()
            elif cmd == '2':
                c2.edit_prompt()
            elif cmd == 'i':
                interactive = False
                break
            elif cmd == 'q':
                running = False
                break

    return 0


if __name__ == "__main__":
    exit(main())

