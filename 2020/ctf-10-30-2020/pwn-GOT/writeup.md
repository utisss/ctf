# GOT
* **Event:** SpookyCTF (ISSS CTF 10-28-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

[GOT](https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html) useful target for arbitrary write exploits

## Exploit
```
This binary gives us an arbitrary write. The easiest target for this is overwriting the GOT.

If we overwrite the GOT entry for puts() with get_shell(), we will call get_shell instead of puts.

See the exploit script for more info.
```
