# Library
The binary gives you the address of `system` and `"/bin/sh"`. Buffer overflow to a `pop rdi; ret` gadget to set `rdi` to
`"/bin/sh"`, then jump to system to get a shell
