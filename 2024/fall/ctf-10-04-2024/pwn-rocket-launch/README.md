# Rocket Launch
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Binary Exploitation

## Background

[Buffer overflow](https://en.wikipedia.org/wiki/Buffer_overflow)

## Exploit

We are given an interface where we can type something, but it seems that every time we press enter,
nothing happens and we are just stuck in an infinite loop. By analyzing the binary, we can deduce
that the goal of this problem is to exit the while loop and therefore the child process, and then
the parent process will give us the flag. Notably, we don't care how the child process ends, as long
as it does end. Conveniently the child process handles the enter press by reading input into a
buffer of size 100. By typing something longer than 100 characters, we can overflow this buffer and
eventually overwrite the return address of the rocket function into garbage, causing the process to
crash.