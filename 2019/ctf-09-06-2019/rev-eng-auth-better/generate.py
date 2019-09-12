#!/usr/bin/env python
import random
flag = "utflag{UmVhZCB0aGlzOiBodHRwczovL2FyeGl2Lm9yZy9hYnMvMTkwMy4wODU3MA==}"
rand = [random.randint(1,200) for i in range(len(flag))]

for idx, b in enumerate(rand):
    print(f"pad[{idx}] = {b};")
store = [(ord(ch) ^ ran) for ch,ran in zip(flag,rand)] 
for idx, b in enumerate(store):
    print(f"store[{idx}] = {b};")

print("\nValidating\n")

print("".join([chr(c1 ^ c2) for c1,c2 in zip(rand,store)]))

print(str(len(flag)))
