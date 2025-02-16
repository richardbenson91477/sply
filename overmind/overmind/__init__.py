
state = "Here's some module global state."

def hello (self):
    print(f"Hello, world from {self}! {state}")

from .node import node

node.hello = hello

state = "Here's some modified module global state."

