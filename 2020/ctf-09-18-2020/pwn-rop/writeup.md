# Overflow
* **Event:** TetrisCTF (ISSS CTF 09-19-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Exploit
```
A buffer overflow is a common binary exploitation technique. The stack frame saves the return address at rbp+0x8.

In this case we also need to ensure that RDI=0x1337 when calling get_shell. We just find a `pop rdi; ret` gadget in the binary and use that.

Our buffer is at rbp-0x70. If we fill the buffer with 0x78*b'a' + POP_RDI + 0x1337 + addr_of_get_shell we'll get a shell.
```
