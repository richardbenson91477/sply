#!/usr/bin/env python3

class node:
    def __init__ (self, label, msg, runcode=True):
        print(f"node.__init__ (label=\"{label}\", msg=\"{msg}\")")
        self.label = label
        self.msg = msg
        self.d = {}
        if runcode:
            self.sp.runcode(f"{label} = overmind.node(\"{label}\", \"{msg}\")", show=True)

    def __call__ (self, msg):
        print(f"node.__call__ (msg=\"{msg}\")")
        res = self.sp.runcode(msg, show=True)
        return res

    def __getitem__ (self, item):
        print(f"node.__getitem__ (item=\"{item}\")")
        #self.d[item]
        res = self.sp.runcode(f"{self.label}[\"{item}\"]", show=True)
        return res

    def __setitem__ (self, item, val):
        print(f"node.__setitem__ (item=\"{item}\", val=\"{val}\")")
        self.d[item] = val
        self.sp.runcode(f"{self.label}[\"{item}\"] = \"{val}\"", show=True)

    def __add__ (self, val):
        print(f"node.__add__ (val=\"{val}\")")
        return self

    def new (self, label, msg):
        print(f"node.new (label=\"{label}\", msg=\"{msg}\")")
        res = node(label, msg, runcode=False)
        self.sp.runcode(f"{label} = {self.label}.new(\"{label}\", \"{msg}\")", show=True)
        return res

