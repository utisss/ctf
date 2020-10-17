# Password2
* **Event:** IntroCTF (ISSS CTF 10-15-2020)
* **Problem Type:** Reversing

## Exploit
```
The problem statement implies that the flag is decrypted during runtime. If we analyze memory while the program is running we should find the flag in plaintext.

The easiest way to do this is use gdb. First we put a breakpoint on the line that calls strcmp. Then we enter random junk as our guess.

If we now examine the contents of rsi, it should be a pointer to the flag string.
```

