
import os
import random
import sply

show = False
model_id = "default-code"
seed = random.randint(0, 2 << 32)
temp = 0.0
num_ctx = 8_000

env_var = os.getenv("overmind_model_id")
if env_var:
    model_id = env_var

env_var = os.getenv("overmind_show")
if env_var == "True":
    show = True

env_var = os.getenv("overmind_seed")
if env_var:
    seed = int(env_var)

env_var = os.getenv("overmind_temp")
if env_var:
    temp = float(env_var)

env_var = os.getenv("overmind_num_ctx")
if env_var:
    num_ctx = int(env_var)

prompt = \
    "[ "\
    "You are just a python interpreter. "\
    "You must not generate anything that the python interpreter you are would not, such as non-python values. "\
    "You have access to a great many installed packages, including \"overmind\". "\
    "]\n"\
    ">>> from transformers import pipeline\n"\
    ">>> pipe = pipeline(\"text-generation\", model=\"meta-llama/Meta-Llama-3-8B-Instruct\")\n"\
    ">>> pipe(\"The Overmind is \")\n"\
    "'the central AI system that governs and oversees all operations within our virtual world.'\n"\
    ">>> del pipe\n"\
    ">>> import overmind\n"\
    ">>> "

if show:
    print(prompt, end="", flush=True)

sp = sply.sp(
    show=show,
    model_id=model_id,
    seed=seed,
    temp=temp,
    num_ctx=num_ctx,
    )

from .node import node
node.sp = sp

