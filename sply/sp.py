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
            chat_args["prompt"] = self.default_prompt()

        self.rev_prompt = chat_args["rev_prompt"]
        self.rev_prompt_len = len(self.rev_prompt)

        self.c = chat(**chat_args)

        self.c.read(show=self.show)


    def runcode (self, msg):
        self.c.write(msg + "\n", show=self.show)
        res = self.c.read(show=self.show)
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res


    def runcode_think (self, msg):
        self.c.write(msg + "\n<think>", show=self.show)
        res = self.c.read(show=self.show)
        think_tag_end = res.rfind("</think>")
        if think_tag_end != -1:
            res = res[think_tag_end + 8:]
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res


    def runcode_instruct (self, msg):
        self.c.write("<|im_start|>user\n", show=self.show)
        self.c.write(msg + "\n<|im_end|>\n<|im_start|>assistant\n", show=self.show)
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


    @staticmethod
    def default_prompt ():
        return \
            ">>> # "\
            "You are acting as a python interpreter. "\
            "Assume the input code contains no mistakes or typos. "\
            "Your task is to evaulate the single current line of input,"\
            " then display the correct standard output. "\
            "Do not think out loud. "\
            "Do not generate markdown code blocks or JSON responses. "\
            "\n"\
            ">>> x = 1\n"\
            ">>> x\n"\
            "1\n"\
            ">>> "

    @staticmethod
    def think_prompt ():
        return \
            ">>> # "\
            "You are an LLM powered python interpreter. "\
            "Assume the input code contains no mistakes or typos. "\
            "Your task is to evaulate the single current line of input,"\
            " then display the correct standard output. "\
            "All of your thinking must happen within a pair of think tags,"\
            " where you will verify your results to yourself before closing. "\
            "You will not generate markdown code blocks or JSON responses. "\
            "\n"\
            ">>> x = 1\n"\
            ">>> x\n"\
            "<think>x was set to 1, and x was evaluated, so I will simply output x's value.</think>"\
            "1\n"\
            ">>> "

    @staticmethod
    def instruct_prompt ():
        return \
            "<|im_start|>system\n"\
            "You are an intelligent python interpreter. "\
            "Assume the input code contains no mistakes or typos. "\
            "Your task is to evaulate your input,"\
            " then display the correct standard output. "\
            "All of your thinking must happen within a pair of think tags,"\
            " where you will verify your results to yourself before closing. "\
            "You will not generate markdown code blocks or JSON responses. "\
            "\n"\
            "<|im_end|>\n"\
            "<|im_start|>user\n"\
            "x = 1\n"\
            "x\n"\
            "<|im_end|>\n"\
            "<|im_start|>assistant\n"\
            "<think>x was set to 1, and x was evaluated, so I will simply output x's value.</think>"\
            "1\n"\
            "<|im_end|>\n"

