from pwn import *
from sage.all import ecm

# connection details
ADDRESS = 'ctf.isss.io'
PORT = 5423

# implementation specific constants
ENCODING = 'utf-8'

# establish connection
conn = connect(ADDRESS, PORT)

# trash values
conn.recvline()
conn.recvline()
conn.recvline()

# extract challenge
challenge = int(conn.recvline().decode(ENCODING).strip().split()[1])
# extract n
n = int(conn.recvline().decode(ENCODING).strip().split()[-1][:-1])
# extract e
e = int(conn.recvline().decode(ENCODING).strip().split()[-1][:-1])

# split challenge into two factors
challenge_factors = ecm.find_factor(challenge)

signed_factors = []

for _ in range(0, 2):
    # trash values
    conn.recvline()
    conn.recvline()
    conn.recvline()

    # sign value
    conn.sendline(b'1')
    # trash value
    conn.recvline()
    # send factor
    conn.sendline(str(challenge_factors.pop()))
    # extract signed factor and store
    signed_factors.append(int(conn.recvline().decode(ENCODING).strip().split()[-1][:-1]))

# multiple signed factors and reduce modulo n
signed_challenge = (signed_factors[0] * signed_factors[1]) % n

# sign value
conn.sendline(b'2')
# trash values
conn.recvline()
conn.recvline()
conn.recvline()
conn.recvline()

# send answer
conn.sendline(str(signed_challenge))

# print flag
print(conn.recvline().decode(ENCODING).strip().split()[-1][:-1])

# end connection
conn.close()
