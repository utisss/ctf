# Spooky Signature
* **Event:** NightmareCTF (ISSS CTF 10-18-2024)
* **Problem Type:** Cryptography

## Background

[RSA-Based Digital Signatures](https://cryptobook.nakov.com/digital-signatures/rsa-signatures)

["Textbook" RSA](https://joyofcryptography.com/pdf/chap13.pdf)

## Exploit

The goal here is to forge a signature as the adversary in the RSA digital signature scheme. We are
given the source code and can see that the the crucial step of hashing the message is missing.
Without the hashing step, the signature is deterministic, and there are a couple of ways we can
break it. One is by using algebraic properties of message-signature pairs, such as squaring an
existing message. We can also fix some signature and compute the ciphertext for it with the e we are
given, and use that pair as the forgery.