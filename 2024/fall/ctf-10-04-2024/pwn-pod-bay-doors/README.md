# Open the pod bay doors, HAL.
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Binary Exploitation

## Background

[Buffer overflow](https://en.wikipedia.org/wiki/Buffer_overflow)

[Stack layout](https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64/)

[pwntools](https://docs.pwntools.com/en/stable/)

## Exploit

Similarly to Rocket Launch, we are again trying to overflow a buffer. However, this time we don't
need to just crash the program, rather we want to call the get_flag function somehow. We can take
advantage of the fact that the return address of our main function is stored on the stack, and
overwrite that value with the address of get_flag. This can be found through static analysis, and
since ASLR is disabled we can just hard-code the return address we want to override. In order to
send the correct bytes, which may not be human-readable ASCII characters, we can use a Python one-
liner or a library like pwntools to send the bytes for us. A sample solution using pwntools is
provided in sol.py.