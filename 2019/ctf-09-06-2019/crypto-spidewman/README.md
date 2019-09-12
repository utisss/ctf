# Spidewman
* **Event:** BepisCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**
​

## Steps

### Step 1
We notice that we are provided with a files called `encrypt.py` and `ciphertext.py`.
The python program opens a file called `plaintext.txt` and applies the [xor](https://en.wikipedia.org/wiki/XOR_cipher) operation on each byte of the file with a secret value called `key`.
The result is then outputed to the file called `ciphertext.txt`.
Our goal is to reverse the encryption and find out what the original file contained.


#### Step 2
If we find the value of `key` then we can reverse the encryption by using the fact that `(a_i ^ key) ^ key = a_i ^ (key ^ key) = a_i ^ 0 = a_i` where `a_i` is the ith byte of the plaintext file.
Since `(a_i ^ key)` is just the ith byte of the ciphertext file we can simply brute force through all 255 characters and xor the bytes with that character until we find a valid plaintext file.


```python
ciphertext = open('ciphertext.txt', 'r').readlines()[0]
print(ciphertext)
for i in range(1, 256):
    candidate = ''.join([chr(ord(x) ^ ord(chr(i))) for x in ciphertext])
    if 'utflag' in candidate:
        print(candidate, chr(i))
```
