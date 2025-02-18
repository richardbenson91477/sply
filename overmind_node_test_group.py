#!/usr/bin/env python3

import overmind

n = overmind.node("n", "a primary node connected to the Overmind")
jane = n.new("jane", "an intelligent being named Jane, female gender, age 25.")
jane["name"]
n("infer the meaning of a 'realism' property of the jane object and describe it to me")
jane["realism"] = "very high"
jane["IQ"] = "120.0"
user = n.new("user", "a reference to myself, a man named John")
jane["master"] = "user"
jane("how are you feeling today?")
sue = n.new("sue", "Sue - a copy of Jane with various personal properties randomly changed by up to 20%")
sue["master"] = "user"
g = n.new("g", "an empty group that I can communicate with")
g["members"] = ["jane", "sue"]
n.new("room", "a large and luxurious living room")
room = n.new("room", "a large and luxurious living room")
user["location"] = "room"
g["location"] = "room"
n("add some items to the living room that Jane and Sue would like")
print(g("how do you like the room?"))

