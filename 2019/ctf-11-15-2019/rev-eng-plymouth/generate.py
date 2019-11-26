flag = "utflag{l1sten_k1d_w3_d0n't_hav3_much_t1m3_p33_is_actually_stored_in_the_....}"



stuff = [(ord(ch) - 2) ^ 0x33 for ch in flag]
print(stuff)
print(len(flag))
