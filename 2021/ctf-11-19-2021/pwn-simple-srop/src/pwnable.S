        .global _start

        .data
        .asciz "/bin/sh"

        .text
_start:
        call vuln

        # exit
        mov     $60, %rax
        xor     %rdi, %rdi
        syscall          
        ret

vuln:
        push    %rbp
        mov     %rsp, %rbp
        sub     $100, %rsp
        mov     $0, %rax                # read
        mov     $0, %rdi                # stdin
        mov     %rsp, %rsi              # buf
        mov     $0x1000, %rdx            # len
        syscall

        add     $100, %rsp
        pop     %rbp
        ret

srop:
        pop     %rax
        pop     %rbx
        pop     %rcx
        pop     %rdx
        pop     %rdi
        pop     %rsi
        pop     %rbp
        ret
