#!/usr/bin/env python3

import random
from .chat import chat

class sp:
    model_id_def = "default-code"
    rev_prompt_def = "\n>>> "
    options_def = {
        "seed": random.randint(0, 2 << 32),
        "temperature": 0.0,
        "num_ctx": 20_000,
        }

    def __init__ (self,
            show=False,
            model_id="",
            editor="",
            prompt_file="",
            prompt="",
            options=None,
            ):

        self.model_id = model_id if model_id else self.model_id_def

        self.editor = editor

        self.rev_prompt = self.rev_prompt_def
        self.rev_prompt_len = len(self.rev_prompt)

        if prompt_file:
            with open(prompt_file, "r") as f:
                self.prompt = f.read()
        elif prompt:
            self.prompt = prompt
        else:
            self.prompt = self.default_prompt()

        self.options = options if options else self.options_def

        self.c = chat(
            model_id=self.model_id,
            editor=self.editor,
            rev_prompt=self.rev_prompt,
            in_suffix_enabled=False,
            prompt=self.prompt,
            options=self.options,
            )

        self.c.read(show=show)

    def runcode (self, msg, show=False):
        self.c.write(msg + "\n", show=show)
        res = self.c.read(show=show)
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res

    def __getitem__ (self, item):
        pass

    def __setitem__ (self, item, val):
        pass

    def edit_prompt (self):
        self.c.edit_prompt()
        # FIXME: read here?

    def default_prompt (self):
        return "["\
            "You are just a python interpreter."\
            "You must not generate anything that the python interpreter you are would not."\
            "]\n"\
            ">>> x = 6\n"\
            ">>> print(x)\n"\
            "6\n"\
            ">>> y = 3\n"\
            ">>> print(x+y)\n"\
            "9\n"

