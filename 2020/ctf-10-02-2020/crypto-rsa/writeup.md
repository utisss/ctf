# RSA
* **Event:** AmongUsCTF (ISSS CTF 10-02-2020)
* **Problem Type:** Crypto

## Exploit
```
We used N = p^2 in this problem. The main point to notice is that totient(p^2) is (p^2 - p). Notice this is NOT (p-1)^2.

Then we just compute d and undo the encryption.
```
