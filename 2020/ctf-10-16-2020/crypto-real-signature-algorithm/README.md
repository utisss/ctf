# Real Signature Algorithm
* **Event:** Security Day CTF
* **Problem Type:** Crypto
* **Difficulty:** Medium
* **Tools Used:** pwntools

## Solution

Textbook RSA signs a message _m_ with _s = m^d mod n_.
A signature _s_ is verified with _m = s^e mod n_.

_(s1^e mod n) * (s2^e mod n) = (s1 * s2)^e mod n_ 

The service will refuse to sign the challenge. The challenge is a composite number.
Sign both factors of the challenge separately, then multiply the signatures.

The solution script is in `solution.py`
