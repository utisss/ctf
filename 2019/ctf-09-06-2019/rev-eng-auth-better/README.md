# Writeup

This problem was basically just a repeat of rev-eng-auth with some extra steps. By disassembling main, we see that a buffer is being XORd by a byte and used as instructions after it's decrypted. 

>   0x0000000000001159 <+0>:     push   rbp

>   0x000000000000115a <+1>:     mov    rbp,rsp

>   0x000000000000115d <+4>:     sub    rsp,0x350

>   0x0000000000001164 <+11>:    mov    DWORD PTR [rbp-0x344],edi

>   0x000000000000116a <+17>:    mov    QWORD PTR [rbp-0x350],rsi

>   0x0000000000001171 <+24>:    mov    rax,QWORD PTR fs:0x28

>   0x000000000000117a <+33>:    mov    QWORD PTR [rbp-0x8],rax

>   0x000000000000117e <+37>:    xor    eax,eax

>   0x0000000000001180 <+39>:    lea    rdi,[rip+0xe7d]        # 0x2004

>   0x0000000000001187 <+46>:    call   0x1030 <puts@plt>

>   0x000000000000118c <+51>:    mov    rdx,QWORD PTR [rip+0x31ed]        # 0x4380 <stdin@@GLIBC_2.2.5>

>   0x0000000000001193 <+58>:    lea    rax,[rbp-0x330]

>   0x000000000000119a <+65>:    mov    esi,0x50

>   0x000000000000119f <+70>:    mov    rdi,rax

>   0x00000000000011a2 <+73>:    call   0x1050 <fgets@plt>

>   0x00000000000011a7 <+78>:    mov    DWORD PTR [rbp-0x340],0x0

>   0x00000000000011b1 <+88>:    jmp    0x11e4 <main+139>

>   0x00000000000011b3 <+90>:    mov    eax,DWORD PTR [rbp-0x340]

>   0x00000000000011b9 <+96>:    cdqe

>   0x00000000000011bb <+98>:    lea    rdx,[rip+0x2e9e]        # 0x4060 <bytecode> <- dump this to get the bytecode

>   0x00000000000011c2 <+105>:   movzx  eax,BYTE PTR [rax+rdx*1]

>   0x00000000000011c6 <+109>:   xor    eax,0x3

>   0x00000000000011c9 <+112>:   mov    ecx,eax

>   0x00000000000011cb <+114>:   mov    eax,DWORD PTR [rbp-0x340]

>   0x00000000000011d1 <+120>:   cdqe

>   0x00000000000011d3 <+122>:   lea    rdx,[rip+0x2e86]        # 0x4060 <bytecode>

>   0x00000000000011da <+129>:   mov    BYTE PTR [rax+rdx*1],cl

>   0x00000000000011dd <+132>:   add    DWORD PTR [rbp-0x340],0x1

>   0x00000000000011e4 <+139>:   mov    eax,DWORD PTR [rbp-0x340]

>   0x00000000000011ea <+145>:   cmp    eax,0x319

>   0x00000000000011ef <+150>:   jbe    0x11b3 <main+90>

>   0x00000000000011f1 <+152>:   lea    rax,[rip+0x2e68]        # 0x4060 <bytecode>

>   0x00000000000011f8 <+159>:   mov    QWORD PTR [rbp-0x338],rax

>   0x00000000000011ff <+166>:   lea    rax,[rbp-0x330]

>   0x0000000000001206 <+173>:   mov    rdx,QWORD PTR [rbp-0x338] <- creating function pointer to buffer containing bytecode

>   0x000000000000120d <+180>:   mov    rdi,rax 

>   0x0000000000001210 <+183>:   call   rdx  

>   0x0000000000001212 <+185>:   mov    DWORD PTR [rbp-0x33c],eax

>   0x0000000000001218 <+191>:   cmp    DWORD PTR [rbp-0x33c],0x0

>   0x000000000000121f <+198>:   je     0x1234 <main+219>

>   0x0000000000001221 <+200>:   lea    rdi,[rip+0xdeb]        # 0x2013

>   0x0000000000001228 <+207>:   call   0x1030 <puts@plt>

>   0x000000000000122d <+212>:   mov    eax,0x1

>   0x0000000000001232 <+217>:   jmp    0x1245 <main+236>

>   0x0000000000001234 <+219>:   lea    rdi,[rip+0xde8]        # 0x2023

>   0x000000000000123b <+226>:   call   0x1030 <puts@plt>

>   0x0000000000001240 <+231>:   mov    eax,0x0

>   0x0000000000001245 <+236>:   mov    rcx,QWORD PTR [rbp-0x8]

>   0x0000000000001249 <+240>:   xor    rcx,QWORD PTR fs:0x28

>   0x0000000000001252 <+249>:   je     0x1259 <main+256>

>   0x0000000000001254 <+251>:   call   0x1040 <__stack_chk_fail@plt>

>   0x0000000000001259 <+256>:   leave

>   0x000000000000125a <+257>:   ret


The big brain move is to simple set a breakpoint on $call rdx$ and look at the instructions yourself. By looking at the bytecode, you can tell that it basically just does the same thing as the last program, except the encrypted flag and key are created dynamically at runtime. Dump the encrypted flag and the key and plug it into the same program that you probably wrote for rev-eng-auth
