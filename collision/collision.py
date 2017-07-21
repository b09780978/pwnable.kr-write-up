import struct
import os

hashcode = 0x21DD09EC
divide = hashcode/5
last = hashcode - divide * 4
# print divide, last
payload = struct.pack("<I", divide) * 4 + struct.pack("<I", last)
os.system('./col ' + payload)

