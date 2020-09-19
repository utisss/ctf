from pwn import *
import re

# Connection Info
ADDRESS = 'ctf.isss.io'
PORT = 5421

# Strings are UTF-8 encoded
ENCODING = 'utf-8'

# Establish connection
conn = remote(ADDRESS, PORT)

# Solve challenge
# Will end in an exception, but the flag should be printed
while True:
	# Two non question lines
	print(conn.recvline().decode(ENCODING), end='')
	print(conn.recvline().decode(ENCODING), end='')
	
	# Question line
	line = conn.recvline().decode(ENCODING)
	print(line, end='')
	line = re.split('\s+', line)
	
	# Parse question and calculate sum
	sum = 0
	for word in line:
		try:
			sum += int(word)
		except:
			pass
	
	# Reply with result
	conn.send(str(sum).encode(ENCODING) + b'\n')
