p = 28060033
g = 10

A = 21867942
B = 2551619

# solve by brute force searching a
for a in range(1, p):
    if pow(g, a, p) == A:
        print("a: " + str(a))
        print("K: " + str(pow(B, a, p)))
        break

# alternatively, can brute force search for b
# (only need to do 1 and both equally valid)
for b in range(1, p):
    if pow(g, b, p) == B:
        print("b: " + str(b))
        print("K: " + str(pow(A, b, p)))
        break