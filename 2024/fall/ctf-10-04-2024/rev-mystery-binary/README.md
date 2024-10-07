# Mystery Binary
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Reverse Engineering

## Background

[Decompyle++](https://github.com/zrax/pycdc)

## Exploit

If we open the binary file in a hex editor, the header bytes suggest that the file is Python
bytecode, compiled with Python 3.10. Using this knowledge, we can use a decompilation tool like
pycdc to decompile it. After decompiling, we can see that it's just a repeated xoring of parts of
the flag, and we can reapply all the xors to reverse the original xor. A sample solution is provided
in sol.py.