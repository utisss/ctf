 # Really BeAneD Cipher
 * **Event:** legumeCTF
 * **Problem Type:** Reversing / Crypto
 * **Point Value / Difficulty:** Easy...ish
 * **(Optional) Tools Required / Used:** Rev tool (Ghidra), Scripting language

 ## Solution
Rev the cipher tool. Observe that it asks for a (5 character) key and reads the first and last characters (not the null terminator). The characters form f(0) and f(1) of a fibonacci sequence, and each number in sequence is XORed with a character from the flag. Therefore, you can find the correct f(0) and f(1) characters from just XORing the first two characters with the crib, "ut" of "utflag...", giving f(0) = 104 ('h') and f(1) = 111 ('o'), then XOR the rest of the flag.

 ## Flag
utflag{key_of_2_ez_brute}

 ## Note
The whole key doesn't matter, only the first and fifth/last character. I happened to use "hello" to generate this problem.
