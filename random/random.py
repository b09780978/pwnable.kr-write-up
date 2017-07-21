import os

random_value = 0x6b8b4567
xor_result   = 0xdeadbeef
key = random_value ^ xor_result
print "key is:", key
os.system("echo '" + str(key) + "' | ./random")
