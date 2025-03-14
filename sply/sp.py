#!/usr/bin/env python3

import random
from .chat import chat

class sp:
    def __init__ (self,
            show="",
            model_id="",
            editor="",
            prompt_file="",
            prompt="",
            seed="",
            temp="",
            num_ctx="",
            ):

        self.show = show if show != "" \
            else False

        chat_args = {}
        chat_args["model_id"] = model_id if model_id != "" \
            else "default-code"
        chat_args["editor"] = editor
        chat_args["in_suffix_enabled"] = False
        chat_args["rev_prompt"] = "\n>>> "
        chat_args["seed"] = seed if seed != "" \
            else random.randint(0, 2 << 32)
        chat_args["temp"] = temp if temp != "" \
            else 0.0
        chat_args["num_ctx"] = num_ctx

        if prompt_file:
            with open(prompt_file, "r") as f:
                chat_args["prompt"] = f.read()
        elif prompt:
            chat_args["prompt"] = prompt
        else:
            chat_args["prompt"] = self.create_prompt_default()

        self.rev_prompt = chat_args["rev_prompt"]
        self.rev_prompt_len = len(self.rev_prompt)

        self.c = chat(**chat_args)

        self.c.read(show=self.show)


    def runcode (self, msg):
        self.c.write(f"{msg}\n", show=self.show)
        res = self.c.read(show=self.show)
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res


    def runcode_think (self, msg):
        self.c.write(f"{msg}\n<think>", show=self.show)
        res = self.c.read(show=self.show)
        think_tag_end = res.rfind("</think>")
        if think_tag_end != -1:
            res = res[think_tag_end + 8:]
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res


    def runcode_im (self, msg):
        self.c.write(f"<|im_start|>user\n{msg}\n<|im_end|>\n<|im_start|>assistant\n", show=self.show)
        res = self.c.read(show=self.show)
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res


    def runcode_im_think (self, msg):
        self.c.write(f"<|im_start|>user\n{msg}\n<|im_end|>\n<|im_start|>assistant\n", show=self.show)
        res = self.c.read(show=self.show)
        think_tag_end = res.rfind("</think>")
        if think_tag_end != -1:
            res = res[think_tag_end + 8:]
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res


    def edit_prompt (self):
        self.c.edit_prompt()
        res = self.c.read(show=self.show)
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res


    prompt_base = \
        "You are acting as a python interpreter. "\
        "Assume the input code contains no mistakes or typos. "\
        "Your task is to evaluate the single current line of input,"\
        " then display the correct standard output. "\
        "Do not generate markdown code blocks or JSON responses. "

    prompt_think_base = \
        "All of your thinking must happen within a pair of think tags,"\
        " where you must proove and then verify your results before closing.\n"

    prompt_no_think_base = \
        "Do not think out loud.\n"


    @staticmethod
    def create_prompt_default ():
        return \
            ">>> # " + sp.prompt_base + sp.prompt_no_think_base +\
            ">>> x = 1\n"\
            ">>> x\n"\
            "1\n"\
            ">>> "


    @staticmethod
    def create_prompt_think ():
        return \
            ">>> # " + sp.prompt_base + sp.prompt_think_base +\
            ">>> x = 1\n"\
            ">>> x\n"\
            "<think>x was set to 1, and x was evaluated, so I will simply output x's value.</think>"\
            "1\n"\
            ">>> "


    @staticmethod
    def create_prompt_im ():
        return \
            "<|im_start|>system\n" + sp.prompt_base + sp.prompt_no_think_base +\
            "<|im_end|>\n"\
            "<|im_start|>user\n"\
            "x = 1\n"\
            "x\n"\
            "<|im_end|>\n"\
            "<|im_start|>assistant\n"\
            "1\n"\
            "<|im_end|>\n"


    @staticmethod
    def create_prompt_im_think ():
        return \
            "<|im_start|>system\n" + sp.prompt_base + sp.prompt_think_base +\
            "<|im_end|>\n"\
            "<|im_start|>user\n"\
            "x = 1\n"\
            "x\n"\
            "<|im_end|>\n"\
            "<|im_start|>assistant\n"\
            "<think>x was set to 1, and x was evaluated, so I will simply output x's value.</think>"\
            "1\n"\
            "<|im_end|>\n"


