#!/usr/bin/env python3

import sys
import sply

def main ():
    if len(sys.argv) > 1:
        show=True
    else:
        show=False

    sp = sply.sp(show=show)

    sp.runcode("y = 4", show=show)
    s = sp.runcode("y + 2", show=show)
    print(f"**{s}**")

    #s.edit_prompt()

if __name__ == "__main__":
    exit(main())

