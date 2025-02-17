#!/usr/bin/env python3

class node:
    def __init__ (self, label, msg, runcode=True, verbose=False):
        self.verbose = verbose
        if self.verbose:
            print(f"*node.__init__ (label=\"{label}\", msg=\"{msg}\")*")
        self.label = label
        self.msg = msg
        self.d_r = {}
        self.d_s = {}
        if runcode:
            self.sp.runcode(f"{label} = overmind.node(\"{label}\", \"{msg}\")")

    def __call__ (self, msg):
        if self.verbose:
            print(f"*node.__call__ (msg=\"{msg}\")*")
        res = self.sp.runcode(f"{self.label}(\"{msg}\")")
        return res

    def __setitem__ (self, item, val):
        if self.verbose:
            print(f"*node.__setitem__ (item=\"{item}\", val=\"{val}\")*")
        self.d_r[item] = val
        self.sp.runcode(f"{self.label}[\"{item}\"] = \"{val}\"")

    def __getitem__ (self, item):
        if self.verbose:
            print(f"*node.__getitem__ (item=\"{item}\")*")
        self.d_s = self.sp.runcode(f"{self.label}[\"{item}\"]")
        return self.d_s

    def new (self, label, msg):
        if self.verbose:
            print(f"*node.new (label=\"{label}\", msg=\"{msg}\")*")
        res = node(label, msg, runcode=False, verbose=self.verbose)
        self.sp.runcode(f"{label} = {self.label}.new(\"{label}\", \"{msg}\")")
        return res

