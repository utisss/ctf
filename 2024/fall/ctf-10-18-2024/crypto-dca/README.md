# DCA
* **Event:** NightmareCTF (ISSS CTF 10-18-2024)
* **Problem Type:** Cryptography

## Background

[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

[Euler's Totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)

## Exploit

The challenge text hints to the fact that instead of picking two primes as one would normally do for
RSA, we only picked one prime. (Hence N = p^2)

It is pretty easy to factor N because of this, just take the square root (which will not immediately
work in python because the number is still very big, but it's possible), and recover p.

Once p is obtained, we can now compute the totient function so we can find d. However, keep in mind 
that (p-1)(q-1) is a simplified version of the formula, and doesn't apply when p = q. We actually
need to compute p^2 - p. Then, we take the modular multiplicative inverse to get d and decode the 
ciphertext.