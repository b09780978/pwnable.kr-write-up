import subprocess
import os
import socket
import time

# need to type "ln -s /home/input2/flag flag"
# since input.c command cat flag and flag in /home/input2/flag
# so need link it to current position

# DEBUG = False
DEBUG = True

# stage 1: argv
if not DEBUG:
    args = ['/home/input2/input'] + ['A']*99
else:
    args = ['./input'] + ['A']*99
args[ord('A')] = ""
args[ord('B')] = "\x20\x0a\x0d"
args[ord('C')] = "12345"

# stage 2: stdio
stderr, stderw = os.pipe()

# stage 3: env
env = os.environ.copy()
env["\xde\xad\xbe\xef"] = "\xca\xfe\xba\xbe"
# print env['PATH']

# stage 4: file
f = open("\x0a", "wb")
f.write("\x00\x00\x00\x00")
f.close()

# stage 5: network
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

proc = subprocess.Popen(args, stdin=subprocess.PIPE, stderr=stderr, env=env)
proc.stdin.write("\x00\x0a\x00\xff")

os.write(stderw, "\x00\x0a\x02\xff")

time.sleep(3) # wait input create socket

s.connect(("127.0.0.1", 12345))
s.send("\xde\xad\xbe\xef")
s.close()
