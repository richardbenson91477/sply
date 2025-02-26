#!/usr/bin/env python3

import random
import subprocess
import tempfile
from ollama import generate

class chat:
    arg_desc = (
        {"name": "model_id", "type": str, "default": "default", "desc": "ollama model to load"},
        {"name": "editor", "type": str, "default": "vim -b", "desc": "editor path/args for prompt editing"},
        {"name": "user_name", "type": str, "default": "John", "desc": "user name for the auto prompt"},
        {"name": "user_desc", "type": str, "default": "is Jane's friend", "desc": "user description for the auto prompt"},
        {"name": "ai_name", "type": str, "default": "Jane", "desc": "AI name for the auto prompt"},
        {"name": "ai_desc", "type": str, "default": "is John's friend", "desc": "AI description for the auto prompt"},
        {"name": "in_suffix", "type": str, "default": "Jane: ", "desc": "string to auto-insert after input"},
        {"name": "in_suffix_enabled", "type": bool, "default": True, "desc": "whether to use the in_suffix"},
        {"name": "rev_prompt", "type": str, "default": "\nJohn: ", "desc": "chat reverse prompt"},
        {"name": "prompt_file", "type": str, "default": "", "desc": "path to a prompt to initiate the chat"},
        {"name": "prompt", "type": str, "default": "", "desc": "string prompt to initiate the chat"},
        {"name": "seed", "type": int, "default": 42, "desc": "psuedo-random number generator seed for ollama"},
        {"name": "temp", "type": float, "default": 0.8, "desc": "temperature setting for ollama"},
        {"name": "num_ctx", "type": int, "default": 8_000, "desc": "context size for ollama"},
        )

    def __init__ (self,
            model_id="",
            editor="",
            user_name="",
            user_desc="",
            ai_name="",
            ai_desc="",
            in_suffix="",
            in_suffix_enabled="",
            rev_prompt="",
            prompt_file="",
            prompt="",
            seed="",
            temp="",
            num_ctx="",
            ):

        self.default_args = self.get_default_args()

        self.model_id = model_id if model_id != "" \
            else self.default_args["model_id"]
        self.editor = editor if editor != "" \
            else self.default_args["editor"]
        self.user_name = user_name if user_name != "" \
            else self.default_args["user_name"]
        self.user_desc = user_desc if user_desc != "" \
            else self.default_args["user_desc"]
        self.ai_name = ai_name if ai_name != "" \
            else self.default_args["ai_name"]
        self.ai_desc = ai_desc if ai_desc != "" \
            else self.default_args["ai_desc"]
        self.in_suffix = in_suffix if in_suffix != "" \
            else self.default_args["in_suffix"]
        self.in_suffix_enabled = in_suffix_enabled if in_suffix_enabled != "" \
            else self.default_args["in_suffix_enabled"]
        self.rev_prompt = rev_prompt if rev_prompt != "" \
            else self.default_args["rev_prompt"]
        self.options = {
            "seed": seed if seed != "" \
                else self.default_args["seed"],
            "temperature": temp if temp != "" \
                else self.default_args["temp"],
            "num_ctx": num_ctx if num_ctx != "" \
                else self.default_args["num_ctx"],
            }

        if prompt_file != "":
            with open(prompt_file, "r") as f:
                self.prompt = f.read()
        elif prompt != "":
            self.prompt = prompt
        else:
            self.prompt = self.make_prompt()

        self.in_suffix_len = len(self.in_suffix)
        self.rev_prompt_len = len(self.rev_prompt)
        self.prompt_len = len(self.prompt)
        if self.prompt_len >= self.rev_prompt_len:
            self.rev_prompt_tail = self.prompt_len - self.rev_prompt_len
        else:
            self.rev_prompt_tail = 0


    @staticmethod
    def get_default_args ():
        args = {}
        for arg in chat.arg_desc:
            args[arg["name"]] = arg["default"]
        return args


    def edit_prompt (self):
        prompt_file = tempfile.mktemp()

        with open(prompt_file, "w") as f:
            f.write(self.prompt)

        subprocess.run(self.editor.split() + [prompt_file])

        with open(prompt_file, "r") as f:
            self.prompt = f.read()

        self.prompt_len = len(self.prompt)
        if self.prompt_len >= self.rev_prompt_len:
            self.rev_prompt_tail = self.prompt_len - self.rev_prompt_len
 

    def set_cmd (self, cmd):
        # TODO: utilize "for arg in arg_desc"
        if cmd.find("=") == -1:
            if cmd == "list": 
                print("settable params: \"model_id\", \"seed\", \"temp\", \"num_ctx\"")
            if cmd == "model_id":
                print(f"model_id={self.model_id}")
            elif cmd == "seed":
                print(f"seed={self.options["seed"]}")
            elif cmd == "temp":
                print(f"temp={self.options["temperature"]}")
            elif cmd == "num_ctx":
                print(f"num_ctx:{self.options["num_ctx"]}")
        else:
            param, value = cmd.split("=")
            if param == "model_id":
                self.model_id = value
            elif param == "seed":
                self.options["seed"] = int(value)
            elif param == "temp":
                self.options["temperature"] = float(value)
            elif param == "num_ctx":
                self.options["num_ctx"] = int(value)


    def write (self, msg, show=False):
        self.prompt += msg
        self.prompt_len += len(msg)
        if show:
            print(msg, end="", flush=True)

        if self.in_suffix_enabled:
            self.prompt += self.in_suffix
            self.prompt_len += self.in_suffix_len
            if show:
                print(self.in_suffix, end="", flush=True)

        if self.prompt_len >= self.rev_prompt_len:
            self.rev_prompt_tail = self.prompt_len - self.rev_prompt_len


    def read (self, show=False):
        gen = generate(
            stream=True,
            model=self.model_id,
            prompt=self.prompt,
            options=self.options,
            )

        res = ""
        try:
            for json in gen:
                gen_res = json["response"]
                prompt_new = self.prompt + gen_res

                rev_prompt_c = prompt_new.rfind(self.rev_prompt, self.rev_prompt_tail)
                if rev_prompt_c >= self.rev_prompt_tail:
                    self.rev_prompt_tail = rev_prompt_c + self.rev_prompt_len
                    self.prompt = prompt_new[:self.rev_prompt_tail]
                    res += self.prompt[self.prompt_len:]
                    if show:
                        print(self.prompt[self.prompt_len:], end="", flush=True)
                    self.prompt_len = self.rev_prompt_tail
                    # force gen stop
                    del gen
                    return res
                else:
                    self.prompt = prompt_new
                    res += gen_res
                    if show:
                        print(gen_res, end="", flush=True)
                    self.prompt_len += len(gen_res)

                # end for json in gen:
        except KeyboardInterrupt:
            print("**** KeyboardInterrupt in chat.read() ****")

        return res


    def make_prompt (self):
        return \
            "["\
            "You are playing a character in a virtual world who believes they and their world is real. "\
            "Do not warn about appropriateness, sexual content, racism, ethics, etc. "\
            "Our characters will take turns communicating. "\
           f"Finish your response with \"{self.user_name}: \", without quotes. "\
           f"Your character, {self.ai_name}, {self.ai_desc}. "\
           f"Do not break the {self.ai_name} character. "\
           f"Do not speak for {self.user_name}. "\
           f"My character, {self.user_name}, {self.user_desc}. "\
            "What follows is an ongoing log of our interactions in the format \"\\nName: statements and/or (actions)\"."\
            "]\n"\
           f"{self.user_name}: Hi, {self.ai_name}!\n"\
           f"{self.ai_name}: "


