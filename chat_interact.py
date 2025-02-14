#!/usr/bin/env python3

import random
import sys
import sply

def print_cmds ():
    print("\n*commands*")
    print("/?: this help")
    print("/p: display prompt")
    print("/i: print input")
    print("/c: clear input")
    print("//: input /\\n")
    print("/q: quit")
    print("/e: edit prompt")

def main ():
    model_id = "default"
    editor = ""
    user_name = ""
    user_desc = ""
    ai_name = ""
    ai_desc = "" 
    in_suffix = ""
    in_suffix_enabled = True
    rev_prompt = ""
    prompt_file = ""
    prompt = ""
    options = {
        "seed": random.randint(0, 2 << 32),
        "temperature": 0.8,
        "num_ctx": 5_000,
        }

    if len(sys.argv) > 1:
        for argv in sys.argv[1:]:
            if argv.find("model_id=") == 0:
                model_id = argv[9:]
            if argv.find("editor=") == 0:
                editor = argv[7:]
            if argv.find("user_name=") == 0:
                user_name = argv[10:]
            if argv.find("user_desc=") == 0:
                user_desc = argv[10:]
            if argv.find("ai_name=") == 0:
                ai_name = argv[8:]
            if argv.find("ai_desc=") == 0:
                ai_desc = argv[8:]
            if argv.find("in_suffix=") == 0:
                in_suffix = argv[10:]
            if argv.find("in_suffix_enabled=") == 0:
                in_suffix_enabled = False if argv[18:] == "False" else True
            if argv.find("rev_prompt=") == 0:
                rev_prompt = argv[11:]
            if argv.find("prompt_file=") == 0:
                prompt_file = argv[12:]
            if argv.find("prompt=") == 0:
                prompt = argv[7:]

            if argv.find("seed=") == 0:
                options["seed"] = float(argv[5:])
            if argv.find("temperature=") == 0:
                options["temperature"] = float(argv[12:])
            if argv.find("num_ctx=") == 0:
                options["num_ctx"] = float(argv[8:])

    c = sply.chat(
        model_id=model_id,
        editor=editor,
        user_name=user_name,
        user_desc=user_desc,
        ai_name=ai_name,
        ai_desc=ai_desc,
        in_suffix=in_suffix,
        in_suffix_enabled=in_suffix_enabled,
        rev_prompt=rev_prompt,
        prompt_file=prompt_file,
        prompt=prompt,
        options=options,
        )

    print(c.prompt, end="", flush=True)

    running_ = True
    while running_:
        c.read(show=True)

        add = ""
        while True:
            inp = input()
            if not inp:
                add += "\n"
                break
            elif inp[0] == "/" and len(inp) == 2:
                if inp == "/?":
                    print_cmds()
                    continue
                elif inp == "/p":
                    print("**" + c.prompt + "**")
                    continue
                elif inp == "/i":
                    print("***" + add + "***")
                    continue
                elif inp == "/c":
                    add = ""
                    continue
                elif inp == "//":
                    inp = "/\n"
                    break
                elif inp == "/q":
                    running_ = False
                    break
                elif inp == "/e":
                    c.edit_prompt()
                    add = ""
                    break
                else:
                    print_cmds()
                    continue

            inp_tail = len(inp) - 1
            if inp[inp_tail] == "\\":
                add += inp[:inp_tail] + "\n"
            else:
                add += inp + "\n"
                break
            # end while True

        if not running_:
            break

        if add:
            c.write(add)
            if in_suffix_enabled:
                print(c.in_suffix, end="", flush=True)
        # end while running_

if __name__ == "__main__":
    exit(main())

