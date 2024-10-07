a = b'u\x01g\x0bj\rv\x15%H8\teV2m\x1dd\x10xH&['
sol = []
for i in range(len(a) - 1, 0, -1):
    sol.append(a[i] ^ a[i-1])
sol.append(a[0])
sol.reverse()
print([chr(i) for i in sol])