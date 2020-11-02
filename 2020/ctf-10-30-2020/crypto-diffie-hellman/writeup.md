# Diffie Hellman
# Difficulty: Easy

Here's a quick explanation of the Diffie-Hellman Key Exchange protocol: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Cryptographic_explanation

We are given that the base is 7 and the modulus is 999331 (the base must 
always be strictly less than the modulus). Then according to the protocol
we are given 7^a and 7^b (mod 999331). We can solve for a and b using the 
discrete logarithm since 999331 is a very small modulus. 

Using this calculator, inputting 7 as the base, 999331 as the modulus, and 
858076 as the power, we get that Alice's private secret is 993. We can then
calculate (346579 ^ 993) (mod 999331) to get the shared secret, by following
the steps laid out in the Wikipedia explanation.