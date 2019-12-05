# RSA
* **Event:** DivCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** Python

## Steps​
Since n is small (under 10 digits) we can simply factor the number into p*q using an online tool or by writing a Python script. Then we can calculate phi(n) = (p-1)(q-1), then use a script found online to calculate d, the multiplicative inverse of e mod phi(n). Then we can calculate (c ** d) mod n to derive the original message m for each ciphertext given. Converting each message to a single ASCII character gets us the flag. 