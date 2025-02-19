
import os
import random
import sply

model_id = "default-code"
options = {
    "seed": random.randint(0, 2 << 32),
    "temperature": 0.0,
    "num_ctx": 8_000,
    }
show = False

env_var = os.getenv("overmind_model_id")
if env_var:
    model_id = env_var

env_var = os.getenv("overmind_show")
if env_var == "True":
    show = True

env_var = os.getenv("overmind_seed")
if env_var:
    options["seed"] = int(env_var)

env_var = os.getenv("overmind_temp")
if env_var:
    options["temperature"] = float(env_var)

env_var = os.getenv("overmind_num_ctx")
if env_var:
    options["num_ctx"] = int(env_var)

prompt = \
    "["\
    "You are just a python interpreter. "\
    "You must not generate anything that the python interpreter you are would not. "\
    "]\n"\
    ">>> from transformers import pipeline\n"\
    ">>> pipe = pipeline(\"text-generation\", model=\"meta-llama/Meta-Llama-3-8B-Instruct\")\n"\
    ">>> pipe(\"The Overmind is \")\n"\
    "'The Overmind is the central AI system that governs and oversees all operations within our virtual world.'\n"\
    ">>> del pipe\n"\
    ">>> import overmind\n"\
    ">>> "

if show:
    print(prompt, end="", flush=True)

sp = sply.sp(
    show=show,
    model_id=model_id,
    options=options,
    prompt=prompt,
    )

from .node import node
node.sp = sp

