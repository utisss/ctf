# Vicious Vigenere
* **Event:** NightmareCTF (ISSS CTF 10-18-2024)
* **Problem Type:** Cryptography

## Background

[Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

## Exploit

We are told that the challenge is possible. If the key was the same length as the entire ciphertext,
then the problem wouldn't be possible as it would be an OTP. So the next logical thing is to assume
that the key is 6 characters or fewer long, since we know what the first 6 characters should be
('utflag'). If we figure out what key encodes "kvgsdy" to "utflag", and try decoding the whole
ciphertext with the key, we get the flag.