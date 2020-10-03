# ECDLP
* **Event:** AmongUsCTF (ISSS CTF 10-02-2020)
* **Problem Type:** Crypto

## Background
[Elliptic Curves](https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication) are crazy math.

## Exploit
```
We used an elliptic curve defined on a modular ring instead of a galois field. This is actually equivalent to an elliptic curve defined on GF(p) for each prime factor of the modulus.

We can use this fact to solve the elliptic curve discrete log problem on each prime factor, then recombine them into an end result using the chinese remainder theorem.
```
