# A000073
* **Event:** Spooky (ISSS CTF 10-28-2020)
* **Problem Type:** Reversing

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Cutter](https://cutter.re/) Useful for analyzing binaries

## Exploit
```
This binary xors each byte of the flag with A000073(10*i).

A000073 is the tribonacci sequence. To solve the challenge we need to write an efficient tribonacci algorithm then mod each byte of the encoded flag with trib(i*10) MOD 256.
```
