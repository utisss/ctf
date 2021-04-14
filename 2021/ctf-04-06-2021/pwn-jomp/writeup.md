We have a trivial buffer overflow, from this we can jump to a ropchain of `pop rdi; ret;` and `pop rsi; ret` gadgets to
set the registers. Then just jump to get_flag and win
