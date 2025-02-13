#!/usr/bin/env python3

class node:
    init_msg_def="default init message goes here"

    def __init__ (self, msg=""):
        print("node.__init__")

        if msg:
            self.init_msg = msg
        else:
            self.init_msg = self.init_msg_def

        self.d = {}
        pass

    def __call__ (self, msg):
        print("node.__call__")
        res = f"your msg was {msg}"
        return res

    def __getitem__ (self, item):
        print("node.__getitem__")
        return self.d[item]

    def __setitem__ (self, item, val):
        print("node.__setitem__")
        self.d[item] = val

    def __add__ (self, val):
        print("node.__add__")
        return self

    def new (self, msg):
        print("node.new")
        res = node()
        return res

