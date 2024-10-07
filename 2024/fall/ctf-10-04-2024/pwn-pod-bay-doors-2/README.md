# Open the pod bay doors, HAL. 2
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Binary Exploitation

## Background

[Format string vulnerabilities](https://cs155.stanford.edu/papers/formatstring-1.2.pdf)

[Stack layout](https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64/)

[pwntools](https://docs.pwntools.com/en/stable/)

## Exploit

The structure of this program looks similar to the last, but the vulnerability is different. Here,
we directly call printf with a user-supplied string. This is dangerous because if the user-supplied
string contains format characters, printf will attempt to read those arguments even though they are
not there. In x86, arguments are passed on the stack, so a string with many %xs can essentially dump
stack memory. The flag is located there, so by going far enough we will hit the stack frame of main
and find the flag. A sample solution is provided in sol.py.