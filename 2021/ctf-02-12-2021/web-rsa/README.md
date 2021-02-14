# RSA to $420.69
* **Event:** StonksCTF
* **Problem: Type:** Web
* **Difficulty:** Medium

## Background
RSA is an asymmetric cryptosystem meaning that a public key is used to 
encrypt the message but a private key is needed to decrypt it. It is very
hard to derive the private key given only the public key. 

#### Solution
We view the source code of the website to discover that it is encrypting our 
input with textbook RSA and comparing the encrypted message to the 
encrypted flag. key.js contains p, q, and e, which is all we need to derive
the private key (the public key contains n = p * q instead of p and q 
separately as we have here). We calculate Phi(n) = (p-1) * (q-1) and 
calculate d = e ^ -1 (mod Phi(n)). Raise the encrypted flag to d (mod n) to
decrypt the flag. 