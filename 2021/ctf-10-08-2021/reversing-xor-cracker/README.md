# Reversing: Optimal Encryption
This problem gives an "encrypted" messgae, and the code used to encrypt it. 

The hint is meant to guide you towards reversing each step of the encryption, in reverse order that
they occur in the code. The base64 encoding needs to be undone first, then the XORs and additions 
can be reversed using the commutative property (`a * b = b * a`), as long as you get your for loops 
to go in reverse of the original order.

The random variable `b` is tricky, but can guessed. `b` can only be a number from 0 to 127, so you 
can brute force guess the value of `b`. `decrypt.py` shows a possible way to decrypt the message.

