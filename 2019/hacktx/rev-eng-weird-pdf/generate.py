flag = "utflag{k1nda_drunk_rn_idk_what_t0_put_here}"



stuff = [(ord(ch) - 3) ^ 33 for ch in flag]
print(stuff)
print(len(flag))
