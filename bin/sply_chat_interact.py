#!/usr/bin/env python3

import sys
import random
import sply


def print_cmds ():
    print("\n* commands:\n"
          "/?: this help\n"
          "/p: display prompt (surrounded by **'s)\n"
          "/i: display current input (surrounded by ***'s)\n"
          "/c: clear current input\n"
          "/a: list adjustable params\n"
          "/a param: show param\n"
          "/a param=value: adjust param to value\n"
          "//: input /\\n\n"
          "/e: edit prompt\n"
          "/q: quit\n"
          "*")


def print_usage ():
    default_args = sply.chat.get_default_args()
    print(f"Usage: {sys.argv[0]} [options]\n"
          f"  where [options] are zero or more of:"
          )
    for arg in sply.chat.arg_desc:
        print(f"    {arg["name"]}=({arg["type"].__name__}): "
              f"{arg["desc"]} (default: \"{default_args[arg["name"]]}\")"
              )


def main ():
    chat_args = sply.chat.get_default_args()

    for argv in sys.argv[1:]:
        if argv.find("--help") == 0:
            print_usage()
            exit(-1)
        for arg in sply.chat.arg_desc:
            name = arg["name"]
            tp = arg["type"]
            if argv.find(name + "=") == 0:
                param, value = argv.split("=")
                if tp == str:
                    chat_args[param] = value
                elif tp == bool:
                    chat_args[param] = True if value == "True" else False
                elif tp == int:
                    chat_args[param] = int(value)
                elif tp == float:
                    chat_args[param] = float(value)

    print("chat_args = ", end="")
    print(chat_args)

    c = sply.chat(**chat_args)

    print("")
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
                elif inp == "/a":
                    c.adjust("list")
                    continue
                elif inp == "//":
                    inp = "/\n"
                    break
                elif inp == "/e":
                    c.edit_prompt()
                    add = ""
                    break
                elif inp == "/q":
                    running_ = False
                    break

            elif inp[0:3] == "/a ":
                c.adjust(inp[3:])
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
            if c.in_suffix_enabled:
                print(c.in_suffix, end="", flush=True)
        # end while running_
    return 0


if __name__ == "__main__":
    exit(main())


