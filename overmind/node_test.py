#!/usr/bin/env python3

import overmind

n = overmind.node()

n("what is the overmind?")

jane = n.new("a lady named Jane")

jane["name"] = "Jane"

print(jane["name"])

jane("hello!")

jane += n.new("some delicious snacks")

