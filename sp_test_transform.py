#!/usr/bin/env python3

import sys
# import simulated python link library
import sply

def main ():
    # create a simulated python
    sp = sply.sp(model_id="default-code")

    # set realish y's value to 1
    y = 1
    # print realish y's value
    print(f"y is {y}")

    # set y in simulated python to realish y + 1
    sp.runcode(f"y = {y} + 1")

    # set realish y's value to simulated y's value
    y = int(sp.runcode("y"))

    # print realish y's value
    print(f"y is {y}")

    #s.edit_prompt()

if __name__ == "__main__":
    exit(main())

