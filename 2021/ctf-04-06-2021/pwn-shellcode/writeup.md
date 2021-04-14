# Shellcode Grandma
* **Difficulty:** Easy
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Exploit
We begin by reverse-engineering the program. By opening it in Ghidra and 
navigating to the main() function, we can get the following decompilation:
```C
undefined8 main(void)
{
  char local_18 [16];
  
  printf("%lx\n",local_18);
  gets(local_18);
  return 0;
}
```

Since gets() performs no bounds checking, we should be able to overflow
the buffer on the stack. We are also conveniently given the address of 
the buffer through the printf. 

Next, we open the program in pwntools:
```python
from pwn import *
e = ELF('a.out')
```

And get the following output:
```
[*] '/home/garrettgu/isss-challenges/2021/spring/ctf-04-06-2021/pwn-shellcode/a.out'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```

So we notice that the stack has no canary and has NX disabled. So we can simply
place some shellcode on the stack and jump to it. 

We can figure out how many characters of padding we need before we get to the 
return address by running the program in GEF and giving it the input:
```
aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkk
```

We see that the program halts execution due to a segfault, with the latest 
instruction being a RET and the latest item on the stack being 
"gggghhhhiiiijjjj". So we check the length of the string preceeding it and
get that we need 24 bytes of padding to overwrite the return address.

Finally, we put everything together, 24 bytes of padding, an address pointing
back to the stack, followed by a nop sled and our shellcode.

The details are in solution.py.