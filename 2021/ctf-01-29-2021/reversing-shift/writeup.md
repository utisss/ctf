# Password
* **Event:** IntroCTF (ISSS CTF 10-15-2020)
* **Problem Type:** Reversing

## Exploit
```
The problem statement implies that the password is a hardcoded string.

If we just look through the binary for ascii-encoded strings, we will eventually find the flag.

The linux tool "strings" automates this process. If we run "strings password", we'll get the flag.
```

