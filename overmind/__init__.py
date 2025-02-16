prompt = \
    "["\
    "You are just a python interpreter. "\
    "You must not generate anything that the python interpreter you are would not. "\
    "]\n"\
    ">>> from transformers import pipeline\n"\
    ">>> pipe = pipeline(\"text-generation\", model=\"meta-llama/Meta-Llama-3-8B-Instruct\")\n"\
    ">>> pipe(\"The OverMind is \")\n"\
    "'The OverMind is the central AI system that governs and oversees all operations within our virtual world.'\n"\
    ">>> del pipe\n"\
    ">>> import overmind\n"\
    ">>> "

print(prompt)

import random
import sply

model_id = "default-code"
options = {
    "seed": random.randint(0, 2 << 32),
    "temperature": 0.0,
    "num_ctx": 1_000,
    }

sp = sply.sp(
    show=True,
    model_id=model_id,
    options=options,
    prompt=prompt,
    )

from .node import node
node.sp = sp

