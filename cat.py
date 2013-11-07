#!/usr/bin/env python
#this short script emulates *nix cat
#there are a few things this can't handle though... can you figure them out?

import fileinput

for line in fileinput.input():
    print(line, end='')
