#!/usr/bin/env python3

class node:
    def __init__ (self, label, msg):
        print(f"node.__init__ (label=\"{label}\", msg=\"{msg}\")")
        self.label = label
        self.msg = msg
        self.d = {}

        self.hello()

    def __call__ (self, msg):
        print(f"node.__call__ (msg=\"{msg}\")")
        res = f"your msg was {msg}"
        return res

    def __getitem__ (self, item):
        print(f"node.__getitem__ (item=\"{item}\")")
        return self.d[item]

    def __setitem__ (self, item, val):
        print(f"node.__setitem__ (item=\"{item}\", val=\"{val}\")")
        self.d[item] = val

    def __add__ (self, val):
        print(f"node.__add__ (val=\"{val}\")")
        return self

    def new (self, label, msg):
        print(f"node.new (label=\"{label}\", msg=\"{msg}\")")
        res = node(label, msg)
        return res

