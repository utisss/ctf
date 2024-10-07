# SHA-26
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Cryptography

## Background
[Hash Function](https://en.wikipedia.org/wiki/Hash_function)

[Simple Hash Algorithm](https://en.wikipedia.org/wiki/SHA-2)

[Pigeonhole Principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)

[Birthday Attack](https://en.wikipedia.org/wiki/Birthday_attack)

## Exploit

This challenge has us essentially trying to find a hash collision in SHA-256. SHA-256 is well known
for being a secure and modern hash with no known collisions since it has 256 bits of entropy, and
trying to brute force for a collision would be inconceivable. However, this challenge purposefully
checks hash equality in a strange way. The typo is in the loop which checks every bit of each hash
against each other; it only checks 26 bits instead of 256. This essentially reduces the problem to
finding a hash collision in a 26-bit hash algorithm, which is small enough to be bruteforceable. All
we need to do is keep generating hashes until we get two whose first 26 bits match each other. By
Pigeonhole principle, we are guaranteed a collision if we check 2^26 + 1 different values. However,
we can probabilistically expect to do better due to the Birthday paradox. A sample solution is
provided in sol.py.