# Real Steel and Aluminum Co. 
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **Tools Used:**
    * NumPy

## Background
[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is a public-private key crytpsystem. A public key can be used to encrypt any message, but in order to decrypt a message, the private key needs to be used. Some basic knowledge of RSA is needed to solve this problem. The examples for encryption and decryption on the Wikipedia articles are a good start.

## Steps
We are given the public key components `n` and `e`. `n` seems to be secure since it is very long. If `n` is small (up to around 20 digits) you can attempt to factor `n` to obtain the private key. In this case, `e` seems more interesting since typically a large enough exponent such as 62235 is used rather than 3. 
In this case, we also know from the problem description that the message is short and unpadded. 
We can use the encryption formula: `c = (m ^ e) mod n` where `^` is the exponentiation operator. Since `m` and `e` are both small and `n` is very large, `m ^ e` is not large enough to exceed the value of n. Thus `c = m ^ e`. Since we are given `c` and `e`, we can obtain `m` by substituting `e = 3` and taking the cube root of both sides. 
The cube root of `c` can be obtained through [numpy.cbrt](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.cbrt.html)