#!/usr/bin/env python3

import random
from .chat import chat

class sp:
    show_def = False
    model_id_def = "default-code"
    editor_def = ""
    rev_prompt_def = "\n>>> "
    seed_def = random.randint(0, 2 << 32)
    temp_def = 0.0
    num_ctx_def = 20_000

    def __init__ (self,
            show=None,
            model_id=None,
            editor=None,
            prompt_file=None,
            prompt=None,
            seed=None,
            temp=None,
            num_ctx_def=None,
            ):

        self.show = show if show is not None \
            else self.show_def

        self.model_id = model_id if model_id is not None \
            else self.model_id_def

        self.editor = editor if editor is not None \
            else self.editor_def

        self.rev_prompt = self.rev_prompt_def
        self.rev_prompt_len = len(self.rev_prompt)

        if prompt_file:
            with open(prompt_file, "r") as f:
                self.prompt = f.read()
        elif prompt:
            self.prompt = prompt
        else:
            self.prompt = self.default_prompt()

        self.seed = seed if seed is not None \
            else self.seed_def

        self.temp = temp if temp is not None \
            else self.temp_def

        self.num_ctx = num_ctx if num_ctx is not None \
            else self.num_ctx_def

        self.c = chat(
            model_id=self.model_id,
            editor=self.editor,
            in_suffix_enabled=False,
            rev_prompt=self.rev_prompt,
            prompt=self.prompt,
            seed=self.seed,
            temp=self.temp,
            num_ctx=self.num_ctx,
            )

        self.c.read(show=self.show)

    def runcode (self, msg):
        self.c.write(msg + "\n", show=self.show)
        res = self.c.read(show=self.show)
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res

    def edit_prompt (self):
        self.c.edit_prompt()
        res = self.c.read(show=self.show)
        if res.rfind(self.rev_prompt) == len(res) - self.rev_prompt_len:
            res = res[:-self.rev_prompt_len]
        return res

    def default_prompt (self):
        return \
            "["\
            "You are just a python interpreter. "\
            "You must not generate anything that the python interpreter you are would not."\
            "]\n"\
            ">>> x = 1\n"\
            ">>> print(x)\n"\
            "1\n"\
            ">>> y = x + 1\n"\
            ">>> print(x+y)\n"\
            "3\n"\
            ">>> del [x, y]\n"

