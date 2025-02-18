#!/usr/bin/env python3

import overmind

n = overmind.node("n", "a primary node connected to the Overmind")
print(n["how many nodes are active?"])

jane = n.new("jane", "a lady named Jane")
jane["name"] = "Jane"
print(jane["name"])

snacks = n.new("snacks", "some delicious snacks")
print(n("give the 'snacks' to 'jane'"))

print(jane("how are you?"))

