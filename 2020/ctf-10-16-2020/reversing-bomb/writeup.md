# Bomb
* **Event:** IntroCTF (ISSS CTF 10-15-2020)
* **Problem Type:** Reversing

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Cutter](https://cutter.re/) Useful for analyzing binaries

## Exploit
```
This problem requires you to reverse several basic math functions.

The first stage takes two ints as input, then checks if their sum is 420.

The second stage takes three ints x,y,z as input and checks z*(x+y) = 69.

The third stage takes two ints as input and checks if 1<<6 = 64.

The best way to approach this problem is probably through Cutter.
```
