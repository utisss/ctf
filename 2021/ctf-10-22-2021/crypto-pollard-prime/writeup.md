# Pollard's Perilous Primes
* **Event:** spoopyCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** 600 (Hard)
* **(Optional) Tools Required / Used:** potentially useful is [this particular online solver](https://www.dcode.fr/prime-factors-decomposition) that uses the Pollard rho method

### Solution
1) As was hinted in the problem description, this RSA problem uses at least one prime that is not safe. (A safe prime p is one where p-1 = 2q, where q is also a prime. In particular, it turns out that for one of the prime factors p, p-1 is a factor of "relatively small" primes...by that I mean the largest is only 11 digits long). The reason we care about this non-safe propery is because there are tricks to factoring a large prime that allow us to exploit that property. One method is [Pollard's P-1 algorithm](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm). You can look at the solution script provided, find a more detailed walk-through of the method [here](https://www.geeksforgeeks.org/pollard-p-1-algorithm/), or use the online solver linked above to figure out how to factor N = pq with p, q primes.
2) Once we have p and q, we can solve for the decryption exponent, d = e^-1 (mod (p-1)(q-1)).
3) Take c^d (mod N) to get the plaintext, then read it as bytes to get the flag.
