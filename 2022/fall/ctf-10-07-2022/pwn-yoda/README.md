# Backwards, I Speak
* **Event:** WiseCTF (ISSS CTF 10-07-2022)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Exploit

This is a slight variation of the standard buffer overflow / ROP attack. By disassembling the binary, we can see that
the `reverse` function reverses the buffer contained by the first argument into the buffer contained by the second
argument. We can control both the first buffer and the length to overflow the output buffer on the stack. This lets
us overwrite the return address of `main` to jump to `get_flag`, which provides shell access.
