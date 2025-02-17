
import os
import random
import sply

model_id = "default-code"
options = {
    "seed": random.randint(0, 2 << 32),
    "temperature": 0.0,
    "num_ctx": 1_000,
    }
show = False

env_model_id = os.getenv("overmind_model_id")
if env_model_id:
    model_id = env_model_id

env_show = os.getenv("overmind_show")
if env_show == "True":
    env_show = True

env_seed = os.getenv("overmind_seed")
if env_seed:
    options["seed"] = int(env_seed)

env_seed = os.getenv("overmind_seed")
if env_seed:
    options["seed"] = int(env_seed)

env_num_ctx = os.getenv("overmind_num_ctx")
if env_num_ctx:
    options["num_ctx"] = int(env_num_ctx)

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

if show:
    print(prompt)

sp = sply.sp(
    show=show,
    model_id=model_id,
    options=options,
    prompt=prompt,
    )

from .node import node
node.sp = sp

