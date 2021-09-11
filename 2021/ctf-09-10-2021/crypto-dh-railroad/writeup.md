# D. & H. Railroad Exchange
* **Event:** monopolyCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** 300 (Meduim)
* **(Optional) Tools Required / Used:**

### Solution
The problem name and description heavily hint that this is a Diffie-Hellman key exchange. Since the prime (p) that Alice and Bob are using is relatively small, we can brute force a search of the possible exponents they chose. 
Alice and Bob have chosen exponents a and b respectively such that g^a = A (mod p) and g^b = B (mod p). You could brute force a search for either exponent, let's say b. Once you've found a value for b where g^b = B (mod p), you could find the key k = (g^a)^b (mod p) = A^b (mod p).
