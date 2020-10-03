# PM_ME_SHELLCODE
# Difficulty: Easy

The goal of this challenge is to write shellcode that calls puts(flag).

Using cutter, we can find that the location of puts in the PLT is 0x1040
and the location of the flag is 0x404040.

Then, we can write the following assembly:
```
mov rdi, 0x404040
mov rax, 0x1040
push 0
jmp rax
```

We add a push in order to ensure the stack is 16-byte aligned. 

Then we simply assemble the code to obtain the shellcode.