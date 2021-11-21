# Crypto: RSA
RSA is a public-key cryptosystem, which means that it uses two keys; one for 
encryption (the public key) and one for decryption (the private key). This is 
useful whenever you want to send someone a message confidentially, since you 
can encrypt with their public key and only people who have their private key 
(which ideally is just them) can decrypt and read the message.

The exploit we want to use for this challenge is the fact that our messages are
not padded before encryption, and that each character is encrypted by itself.
For RSA, it's super important that messages are padded using a secure and
randomized padding scheme.

Essentially, this means that there can only be 256 possible plaintexts, (and 
thus only 256 possible ciphertexts), so we can simply check every possible
character and see if it matches up to each ciphertext.

Here's some code that implements the algorithm:

```python
n = ...
e = ...
c = [...]

flag = ""
for cl in c:
    for i in range(256):
        if pow(i, e, n) == cl:
            flag += chr(i)

print(flag)
```