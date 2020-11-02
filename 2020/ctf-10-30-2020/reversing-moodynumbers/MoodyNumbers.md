```
 # MoodyNumbers
 * **Event:** Among Us CTF
 * **Problem Type:** Reversing
 * **Point Value / Difficulty:** Med (200)
 ## Steps
 #### Step 1
You open the problem in a disassembler and you come across the function that has the following disassembly:
    /*
    0:  66 0f 76 c0             pcmpeqd xmm0,xmm0
    4:  66 0f 3a df c0 01       aeskeygenassist xmm0,xmm0,0x1
    a:  66 0f 3a df c0 02       aeskeygenassist xmm0,xmm0,0x2
    10: 66 0f 3a df c0 03       aeskeygenassist xmm0,xmm0,0x3
    16: 66 0f 3a df c8 04       aeskeygenassist xmm1,xmm0,0x4
    1c: 66 48 0f 7e c8          movq   rax,xmm1
     */
 You notice that the result is moved into rax and used in an XOR operation.
 #### Step 2
At this point, you can either recover the "key" from RAX or try to understand intel's AESKEYGENASSIST instructions.
It's much easier to just set a breakpoint and take the key from RAX.
#### Step 3
You XOR the key with the static buffer found in another function that either prints "correct" or "incorrect"
#### Step 4
You realize that didn't work. To solve here, you need to realize that XOR isn't actually being used. 
There is a not instruction right after the xor instruction, so you need to realize that XNOR is actually being used here.
~(a^b) is XNOR where as (a^b) is XOR. From here you can just XNOR the buffer with the key extracted from RAX.

utflag{e2094fb4675198eb9d48f90fb73d43a596b3de78}
```