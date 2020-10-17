# RSA
* **Event:** TetrisCTF (ISSS CTF 10-15-2020)
* **Problem Type:** Cryptography

## Background
[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is a common crypto system based on the hardness of factoring.

## Exploit
```
RSA assumes that N is not feasibly factorable. In this case, N is even, so p = 2.

Then we just compute d and pt = (ct^d mod N)
```
