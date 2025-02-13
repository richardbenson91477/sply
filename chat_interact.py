#!/usr/bin/env python3

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

    if len(sys.argv) > 1:
        for argv in sys.argv[1:]:
            if argv.find("model_id=") == 0:
                model_id = argv[9:]

    c = sply.chat(model_id=model_id)

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
            print(c.in_suffix, end="", flush=True)
        # end while running_

if __name__ == "__main__":
    exit(main())

