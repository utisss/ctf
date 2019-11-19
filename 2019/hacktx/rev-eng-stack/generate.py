import os
flag = "utflag{I_aM_veRy_sUpr1sed_that_s0m30ne_s01ved_th1s_gj_nerd}"


key = [ch for ch in os.urandom(len(flag))]


check = [ord(c1) ^ c2 for c1,c2 in zip(flag,key)]



print(key)


for i in check:
    print("dq deref_rsi_rax")
    print("dq deref_rdi_rbx")
    print("dq xor_rbx")
    print(f"dq {hex(i)}")
    print("dq check")
    print("dq inc_rsi")
    print("dq inc_rdi\n")

