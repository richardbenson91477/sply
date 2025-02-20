#!/usr/bin/env python3

import overmind

n = overmind.node("n", "a primary node connected to the Overmind")
print(n["return the number of primary nodes online as a string"])

jane = n.node("jane", "a lady named Jane, age 25.")
jane["name"] = "Jane"
print(jane["name"])

snacks = n.node("snacks", "some delicious snacks")
print(n("give the 'snacks' to 'jane'"))

print(jane("What's up?"))

