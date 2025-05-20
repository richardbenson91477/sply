#!/usr/bin/env python3

import sys
import random
import sply
import time

def main ():
    for sys_arg in sys.argv[1:]:
        if sys_arg.find("--help") == 0:
            print_usage()
            exit(-1)
        for param_d in sply.chat.param_desc:
            if sys_arg.find(param_d["name"] + "=") == 0:
                sys_arg_param, sys_arg_value = sys_arg.split("=")
                param_type = param_d["type"]
                if param_type == str:
                    chat_args[sys_arg_param] = sys_arg_value
                elif param_type == bool:
                    chat_args[sys_arg_param] = True if sys_arg_value == "True" else False
                elif param_type == int:
                    chat_args[sys_arg_param] = int(sys_arg_value)
                elif param_type == float:
                    chat_args[sys_arg_param] = float(sys_arg_value)

    print("chat_args = ", end="")
    print(chat_args)
    name_c1 = "Desi"
    name_c2 = "Geni"
    log_path = "desigeni.log"

    c1_args = {
        "backend": "llama-server",
        "port": 8080,
        "user_name": name_c1,
        "user_desc": f"is a brilliant designer who wants to create a game with code by {name_c2}. The game will use no external assets, so that it can be fully designed and tested during the chat. It will have a modern and original design, within reasonable limits",
        "ai_name": name_c2,
        "ai_desc": f"is a programmer who wants to implement {name_c1}'s designs. {name_c2} will use python and pygame, typing out source code for {name_c1} to test",
        "in_suffix": f"{name_c2}:",
        "in_suffix_enabled": False,
        "rev_prompt": f"{name_c1}:",
        "seed": random.randrange(2**32),
        "temp": 0.6,
        "num_ctx": 16384,
        }
    print(f"c1_args={c1_args}")

    c2_args = {
        "backend": "llama-server",
        "port": 8081,
        "user_name": name_c2,
        "user_desc": c1_args["ai_desc"],
        "ai_name": name_c1,
        "ai_desc": c1_args["user_desc"],
        "in_suffix": f"{name_c1}:",
        "in_suffix_enabled": False,
        "rev_prompt": f"{name_c2}:",
        "seed": random.randrange(2**32),
        "temp": 0.9,
        "num_ctx": 16384,
        }
    print(f"c2_args={c2_args}")

    c1 = sply.chat(**c1_args)
    c2 = sply.chat(**c2_args)

    # modify the default prompt's greeting, which is prefaced with '\n'
    c2.prompt = c2.prompt[: c2.prompt.find('\n')] +\
          c2.make_prompt_greet(name_c1, name_c2)
    c2.updated_prompt()

    interactive = False
    interrupted = False
    turn = 1

    running = True
    while running:
        while interactive:
            cmd = input('🔢')
            if not cmd:
                break
            elif cmd == 'h':
                print("  /a: list adjustable params and current values\n"
                print("  /a [param]: display param's value\n"
                print("  /a [param]=[value]: adjust param to value\n"
                print("  /h: this help\n"
                print("  /e1: edit c1 prompt\n"
                print("  /e2: edit c2 prompt\n"
                print("  /p1: display c1 [[prompt]]\n"
                print("  /p2: display c2 [[prompt]]\n"
                # TODO: print help
                pass
            elif cmd == "a": # list adjustable params and current values\n"
          "  /a [param]: display param's value\n"
          "  /a [param]=[value]: adjust param to value\n"
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

        if not running:
            break

        if turn == 1:
            while True:
                in1, interrupted = c1.read(show=True)
                if in1:
                    break
                else:
                    print("", end="", flush=True)
                    time.sleep(1)

            with open(log_path, "a") as f:
                f.write(in1)

            c2.write(in1, show=False)

            if interrupted:
                interrupted = False
                interactive = True
                continue

            # would have to toggle off earlier somehow like c2.write(.., in_suffix=False)
            #if c2.in_suffix_enabled:
            #    c2.write(c2.in_suffix, show=False)
            turn = 2

        if turn == 2:
            while True:
                in2, interrupted = c2.read(show=True)
                if in2:
                    break
                else:
                    print("", end="", flush=True)
                    time.sleep(1)

            with open(log_path, "a") as f:
                f.write(in2)

            c1.write(in2, show=False)

            if interrupted:
                interrupted = False
                interactive = True
                continue

            # would have to toggle off earlier somehow like c2.write(.., in_suffix=False)
            #if c1.in_suffix_enabled:
            #    c1.write(c1.in_suffix, show=False)
            turn = 1


    return 0


if __name__ == "__main__":
    exit(main())

