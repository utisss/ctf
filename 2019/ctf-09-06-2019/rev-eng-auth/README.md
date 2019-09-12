# Writeup

This challenge was pretty much just reversing a simple XOR encryption scheme. By disassembling the main function, one could see that the program reads from stdin, XORs your input by some pad, and compares it to another buffer. Since XOR is a binary operation where its input is its inverse, this implies that one can easily get the original input if one is given the output.

Ex: A \oplus A = id 

Let A \oplus B = C, and notice that A \oplus B \oplus B = C \oplus B is the same as A = C \oplus B

The equivalent statement in our case is <Plaintext> \oplus <Key> = <Ciphertext>. Since we already know the key and the ciphertext, we can construct the plaintext by computing <Ciphertext> \oplus <Key>.


>   0x00000000000011ba <+0>:     push   rbp

>   0x00000000000011bb <+1>:     mov    rbp,rsp

>   0x00000000000011be <+4>:     sub    rsp,0x50

>   0x00000000000011c2 <+8>:     mov    DWORD PTR [rbp-0x44],edi

>   0x00000000000011c5 <+11>:    mov    QWORD PTR [rbp-0x50],rsi

>   0x00000000000011c9 <+15>:    mov    rax,QWORD PTR fs:0x28

>   0x00000000000011d2 <+24>:    mov    QWORD PTR [rbp-0x8],rax

>   0x00000000000011d6 <+28>:    xor    eax,eax

>   0x00000000000011d8 <+30>:    lea    rdi,[rip+0xe3e]        # 0x201d

>   0x00000000000011df <+37>:    call   0x1030 <puts@plt>

>   0x00000000000011e4 <+42>:    mov    rdx,QWORD PTR [rip+0x2ea5]        # 0x4090 <stdin@@GLIBC_2.2.5>

>   0x00000000000011eb <+49>:    lea    rax,[rbp-0x30] <- this is the user buffer

>   0x00000000000011ef <+53>:    mov    esi,0x23

>   0x00000000000011f4 <+58>:    mov    rdi,rax

>   0x00000000000011f7 <+61>:    call   0x1050 <fgets@plt>

>   0x00000000000011fc <+66>:    mov    DWORD PTR [rbp-0x34],0x0

>   0x0000000000001203 <+73>:    jmp    0x1255 <main+155>

>   0x0000000000001205 <+75>:    mov    eax,DWORD PTR [rbp-0x34]

>   0x0000000000001208 <+78>:    cdqe

>   0x000000000000120a <+80>:    lea    rdx,[rip+0x2e3f]        # 0x4050 <store> <- dump this to get the encrypted flag

>   0x0000000000001211 <+87>:    movzx  eax,BYTE PTR [rax+rdx*1]

>   0x0000000000001215 <+91>:    movzx  edx,al

>   0x0000000000001218 <+94>:    mov    eax,DWORD PTR [rbp-0x34]

>   0x000000000000121b <+97>:    cdqe

>   0x000000000000121d <+99>:    movzx  eax,BYTE PTR [rbp+rax*1-0x30]

>   0x0000000000001222 <+104>:   movsx  ecx,al

>   0x0000000000001225 <+107>:   mov    eax,DWORD PTR [rbp-0x34]

>   0x0000000000001228 <+110>:   cdqe

>   0x000000000000122a <+112>:   lea    rsi,[rip+0x2e3f]        # 0x4070 <pad> <- you should dump this to get the key

>   0x0000000000001231 <+119>:   movzx  eax,BYTE PTR [rax+rsi*1]

>   0x0000000000001235 <+123>:   movzx  eax,al

>   0x0000000000001238 <+126>:   xor    eax,ecx <- uWu what is this

>   0x000000000000123a <+128>:   cmp    edx,eax

>   0x000000000000123c <+130>:   je     0x1251 <main+151>

>   0x000000000000123e <+132>:   lea    rdi,[rip+0xde7]        # 0x202c

>   0x0000000000001245 <+139>:   call   0x1030 <puts@plt>

>   0x000000000000124a <+144>:   mov    eax,0x1

>   0x000000000000124f <+149>:   jmp    0x126e <main+180>

>   0x0000000000001251 <+151>:   add    DWORD PTR [rbp-0x34],0x1

>   0x0000000000001255 <+155>:   mov    eax,DWORD PTR [rbp-0x34]

>   0x0000000000001258 <+158>:   cmp    eax,0x1e <- looping over shit

>   0x000000000000125b <+161>:   jbe    0x1205 <main+75>

>   0x000000000000125d <+163>:   lea    rdi,[rip+0xdd7]        # 0x203b

>   0x0000000000001264 <+170>:   call   0x1030 <puts@plt>

>   0x0000000000001269 <+175>:   mov    eax,0x0

>   0x000000000000126e <+180>:   mov    rcx,QWORD PTR [rbp-0x8]

>   0x0000000000001272 <+184>:   xor    rcx,QWORD PTR fs:0x28

>   0x000000000000127b <+193>:   je     0x1282 <main+200>

>   0x000000000000127d <+195>:   call   0x1040 <__stack_chk_fail@plt>

>   0x0000000000001282 <+200>:   leave

>   0x0000000000001283 <+201>:   ret

After you get the encrypted flag and key, just write a simple python script to xor them together.
