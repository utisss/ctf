 # Vigilante Cipher
 * **Event:** robopocalypseCTF
 * **Problem Type:** Crypto
 * **Point Value / Difficulty:** Easy (200 pts)
 * **(Optional) Tools Required / Used:**
## How To Solve
Once you've realized this is a Vigenere Cipher, you've got two main options for how to solve this problem.
#### Option 1 - brute force it a bit
You're given a text file full of possible keys. You could just try every key and see which ones decrypts to something that starts with "utflag...". Careful not to stop your search too soon, though! There's 5 such keys that meet that criteria.

#### Step 2 - work smarter not harder
You already know the first 6 letters of the plaintext should be "utflag", so working backwards, that means that the key must start with "wicked". From there, you can search the word list for any words beginning with "wicked" to find the proper key ("wickedest").
