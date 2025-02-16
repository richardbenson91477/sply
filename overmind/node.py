#!/usr/bin/env python3

class node:
    def __init__ (self, label, msg, runcode=True, show=False):
        self.show = show
        if self.show:
            print(f"*node.__init__ (label=\"{label}\", msg=\"{msg}\")*")
        self.label = label
        self.msg = msg
        self.d_r = {}
        self.d_s = {}
        if runcode:
            self.sp.runcode(f"{label} = overmind.node(\"{label}\", \"{msg}\")", show=self.show)

    def __call__ (self, msg):
        if self.show:
            print(f"*node.__call__ (msg=\"{msg}\")*")
        res = self.sp.runcode(f"{self.label}(\"{msg}\")", show=self.show)
        return res

    def __setitem__ (self, item, val):
        if self.show:
            print(f"*node.__setitem__ (item=\"{item}\", val=\"{val}\")*")
        self.d_r[item] = val
        self.sp.runcode(f"{self.label}[\"{item}\"] = \"{val}\"", show=self.show)

    def __getitem__ (self, item):
        if self.show:
            print(f"*node.__getitem__ (item=\"{item}\")*")
        self.d_s = self.sp.runcode(f"{self.label}[\"{item}\"]", show=self.show)
        return self.d_s

    def __add__ (self, val):
        if self.show:
            print(f"*node.__add__ (val=\"{val}\")*")
        return self

    def new (self, label, msg):
        if self.show:
            print(f"*node.new (label=\"{label}\", msg=\"{msg}\")*")
        res = node(label, msg, runcode=False)
        self.sp.runcode(f"{label} = {self.label}.new(\"{label}\", \"{msg}\")", show=self.show)
        return res

