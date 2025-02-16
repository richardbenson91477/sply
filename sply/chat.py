#!/usr/bin/env python3

import random
import subprocess
import tempfile
from ollama import generate

class chat:
    model_id_def = "default"
    editor_def = "vim"
    user_name_def = "John"
    user_desc_def = "is Jane's friend."
    ai_name_def = "Jane"
    ai_desc_def = "is John's friend." 
    in_suffix_def = "Jane:"
    in_suffix_enabled_def = True
    rev_prompt_def = "\nJohn: "
    options_def = {
        "seed": random.randint(0, 2 << 32),
        "temperature": 0.8,
        "num_ctx": 20_000,
        }

    def __init__ (self,
            model_id="",
            editor="",
            user_name="",
            user_desc="",
            ai_name="",
            ai_desc="",
            in_suffix="",
            in_suffix_enabled=True,
            rev_prompt="",
            prompt_file="",
            prompt="",
            options=None,
            ):

        self.model_id = model_id if model_id else self.model_id_def
        self.editor = editor if editor else self.editor_def
        self.user_name = user_name if user_name else self.user_name_def
        self.user_desc = user_desc if user_desc else self.user_desc_def
        self.ai_name = ai_name if ai_name else self.ai_name_def
        self.ai_desc = ai_desc if ai_desc else self.ai_desc_def

        self.in_suffix = in_suffix if in_suffix else self.in_suffix_def
        self.in_suffix_len = len(self.in_suffix)
        self.in_suffix_enabled = in_suffix_enabled

        self.rev_prompt = rev_prompt if rev_prompt else self.rev_prompt_def
        self.rev_prompt_len = len(self.rev_prompt)
        self.rev_prompt_tail = 0
 
        if prompt_file:
            with open(prompt_file, "r") as f:
                self.prompt = f.read()
        elif prompt:
            self.prompt = prompt
        else:
            self.prompt = self.make_prompt()

        self.prompt_len = len(self.prompt)
        if self.prompt_len >= self.rev_prompt_len:
            self.rev_prompt_tail = self.prompt_len - self.rev_prompt_len

        self.options = options if options else self.options_def

    def edit_prompt (self):
        prompt_path = tempfile.mktemp()

        with open(prompt_path, "w") as f:
            f.write(self.prompt)

        subprocess.run([self.editor, prompt_path])

        with open(prompt_path, "r") as f:
            self.prompt = f.read()

        self.prompt_len = len(self.prompt)
        if self.prompt_len >= self.rev_prompt_len:
            self.rev_prompt_tail = self.prompt_len - self.rev_prompt_len
 
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
           f"Your character, {self.ai_name}, {self.ai_desc} "\
           f"Do not break the {self.ai_name} character. "\
           f"Do not speak for {self.user_name}. "\
           f"My character, {self.user_name}, {self.user_desc} "\
            "What follows is an ongoing log of our interactions in the format \"Name: statements and/or (actions)\"."\
            "]\n"\
           f"{self.user_name}: Hi, {self.ai_name}!\n"\
           f"{self.ai_name}:"

