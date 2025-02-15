#!/usr/bin/env python3

import overmind

n = overmind.node()

n("what is the overmind?")

amy = n.new("a girl named Amy")

amy["name"] = "Amy"

print(amy["name"])

amy("hello!")

amy += n.new("some snacks")

