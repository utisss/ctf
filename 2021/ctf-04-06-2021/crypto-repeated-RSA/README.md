# Repeated RSA
* **Event:** gallacticBattleCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:** 

## Steps
### Step 1
The first thing to do is note is that the problem hints (not very subtley) there's a repeated prime. We can use this to our advantage because it's really hard to factor these big numbers, but finding a common multiple is much easier!

### Step 2
Calculate the greatest common divisor of N1 and N2 to figure out the reused prime. We will call this number p.

### Step 3
You can easily get the other two primes involved by doing q1 = N1 / p and q2 = N2 / p. However, you really only need one or the other since it's the same flag. We'll only need to decrypt once. 

### Step 4
Once you have q1 or q2 (we'll generalize and say the number is just q), you can calculate the totient = (p - 1) * (q - 1) and d = e^-1 (mod totient) (note the "^-1" here means modular inverse).

### Step 5 
Now you can reclaim the flag using flag = c^d (mod N) and interpreting the bytes of that integer in big-endian format.
