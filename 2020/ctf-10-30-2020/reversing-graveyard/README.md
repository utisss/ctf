# Reversing: Ghosts in the Graveyard
This problem gives you a binary, which ask for a password. 
If you disassemble the binary (basically looking at the assembly 
code for the binary) with `objdump -d graveyard`, you can see 
that the main function calls `strcmp()`, which is a C function 
used to compare strings. So the binary must be comparing the 
user's input to some string in the binary to see if it matches. 
The hint suggests using the `strings` utility (installed by 
default on Linux and Mac) to search for this password string. 
You can either just run `strings graveyard` and look through 
all the strings, or get lucky and try 
`strings graveyard | grep password` to find the password string. 

Once you find the password string in the binary, you can use 
it to log onto the server and get the flag.

## Prompt
I just became a ghost, and all the other ghosts won't 
let me into the graveyard! Can you help me find the 
password so I can hang out in the graveyard?

`nc ctf.isss.io 4281`

_by mattyp_

**Include graveyard binary here**

## Hint
Try looking for interesting `strings` in the graveyard.

## Flag
`utflag{now_i_can_spook_like_a_real_ghost}`
