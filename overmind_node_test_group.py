#!/usr/bin/env python3

import overmind
n = overmind.node("n", "a primary node connected to the Overmind")
jane = n.node("jane", "a lady named Jane, age 25.")
jane["name"]
n("infer the meaning of a 'realism' property (i.e. jane['realism']) and return it")
jane["realism"] = "very human-like"
jane["IQ"] = "120.0"
user = n.node("user", "a reference to myself, a man named John")
jane["master"] = "user"
jane("how are you feeling today?")
sue = n.node("sue", "Sue - a copy of Jane with various personal properties randomly changed by up to 20%")
sue["master"] = "user"
g = n.node("g", "an uninitialized node group")
g["members"] = ["jane", "sue"]
room = n.node("room", "a large and luxurious living room")
user["location"] = "room"
g["location"] = "room"
n("add some items to the living room that Jane and Sue would like")
print(g("how do you two like the room?"))

