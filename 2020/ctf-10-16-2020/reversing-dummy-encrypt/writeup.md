# Reversing: Dummy Encrypt
This problem gives an "encrypted" messgae, and the code used to 
encrypt it. The key to this problem is in the hint that XOR is 
commutative and associative. That means that XOR can be inverted, 
and it can be done in any order, i.e. `a ^ (b ^ c) = (a ^ b) ^ c` 
and for `a ^ b = c`, `c ^ b = a`. As a result, almost all the 
encryption code can be used to reverse the encryption. The only 
exception is the base64 encoding, which needs to be undone first, 
and the random variable `b`. However, `b` can only be a number from 
0 to 127, so you can brute force guess the value of `b`. `decrypt.py` 
shows a possible way to decrypt the message.

## Prompt
This cool new messaging app is encrypting their messages end-to-end 
using open-source code called Dummy Encrypt. I stumbled onto an 
encrypted message that seems interesting. Can you decrypt it?

`fGckcjdHQBx0NDEjKwtTFhgaXGRgey4=`

_by mattyp_

## Hint
XOR is commutative _and_ associative!

## Flag
`utflag{respect_the_xor}`
