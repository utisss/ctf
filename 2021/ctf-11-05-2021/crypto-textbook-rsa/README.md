# Textbook RSA
First we notice that c looks very small compared to n. This means that this is
likely an unpadded textbook RSA implementation with a small e. 

We assume that m is too small for m^3 to exceed n, so c = (m^3) mod n = m^3.We 
can simply take the cube root of c to obtain the value of m. 

```python
import gmpy
m3 = 6723702102195566575547896046345427050269402321723710129523169484368725244810477163972859628425061236015708196514825955512567027029431102776329709158005398302454877751909043868477779833957
m3 = gmpy.mpz(int(m3))
m = int(m3.root(3)[0])
print(bytes.fromhex(hex(m)[2:]))
```