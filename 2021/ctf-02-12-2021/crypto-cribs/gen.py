#!/bin/bash

import random

def e(k, m):
	assert(len(k) >= len(m))
	
	return bytes([v for v in map(lambda b:b[0] ^ b[1] , zip(m, k))]).hex()

FLAG = b'utflag{crib dragging can really be an oof}'
M1 = FLAG + b' '
M2 = b' ' + FLAG
KEYLEN = max(len(M1), len(M2))
KEY = random.randbytes(KEYLEN)

print(e(KEY, M1))
print(e(KEY, M2))
