# Overflow
* **Event:** AmongUsCTF (ISSS CTF 10-02-2020)
* **Problem Type:** Reverse Engineering

## Exploit
```
This binary has a pretty simple encoding, throwing it into ghidra or inspecting it in Cutter is easy enough.

We can undo the encoding with the following pseudocode

for i in (0, 64, -1):
    x[i - 1] ^= x[i]
    x[i] -= 5
```
