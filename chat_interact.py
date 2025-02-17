#!/usr/bin/env python3

import sys
import random
import sply

def print_cmds ():
    print("\n* commands:\n"
          "/?: this help\n"
          "/p: display prompt (surrounded by **'s)\n"
          "/i: print current input (surrounded by ***'s)\n"
          "/c: clear current input\n"
          "//: input /\\n\n"
          "/q: quit\n"
          "/e: edit prompt\n"
          "*"
          )

def print_usage ():
    print(f"Usage: {sys.argv[0]} [options]\n"
          f"  where [options] are zero or more of:\n"
          f"    model_id=(string): ollama model to load (default: \"{sply.chat.model_id_def}\")\n"
          f"    editor=(string): editor path for prompt editing (default: \"{sply.chat.editor_def}\")\n"
          f"    user_name=(string): user name for the auto prompt (default: \"{sply.chat.user_name_def}\")\n"
          f"    user_desc=(string): user description for the auto prompt (default: \"{sply.chat.user_desc_def}\")\n"
          f"    ai_name=(string): AI name for the auto prompt (default: \"{sply.chat.ai_name_def}\")\n"
          f"    ai_desc=(string): AI description for the auto prompt (default: \"{sply.chat.ai_desc_def}\")\n"
          f"    in_suffix=(string): string to auto-insert after input (default: \"{sply.chat.in_suffix_def}\")\n"
          f"    in_suffix_enabled=(bool): whether to use the in_suffix (default: {sply.chat.in_suffix_enabled_def})\n"
          f"    rev_prompt=(string): chat reverse prompt (default: \"{sply.chat.rev_prompt_def}\")\n"
          f"    prompt_file=(string): path to a prompt to initiate the chat (default: auto-generated prompt)\n"
          f"    prompt=(string): string prompt to initiate the chat (default: auto-generated prompt)\n"
          f"    seed=(int): psuedo-random number generator seed for ollama (default: random)\n"
          f"    temp=(float): temperature setting for ollama (default: {sply.chat.options_def["temperature"]})\n"
          f"    num_ctx=(int): context size for ollama (default: {sply.chat.options_def["num_ctx"]})\n"
          )

def main ():
    model_id = ""
    editor = ""
    user_name = ""
    user_desc = ""
    ai_name = ""
    ai_desc = "" 
    in_suffix = ""
    in_suffix_enabled = sply.chat.in_suffix_enabled_def
    rev_prompt = ""
    prompt_file = ""
    prompt = ""
    options = sply.chat.options_def

    for argv in sys.argv[1:]:
        if argv.find("--help") == 0:
            print_usage()
            exit(-1)
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
            options["seed"] = int(argv[5:])
        if argv.find("temp=") == 0:
            options["temperature"] = float(argv[12:])
        if argv.find("num_ctx=") == 0:
            options["num_ctx"] = int(argv[8:])
        # end for argv

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

