BITS 64

section .bss
buff resb 0x40


section .text


main:
        push rbp
        mov rbp, rsp
        call pwn
        xor rdi, rdi
        mov rax, 60
        syscall


pwn:
        push rbp
        mov rbp, rsp
        sub rsp, 0x40
        mov rsi, rsp
        xor rax, rax
        xor rdi, rdi
        mov rdx, 0x200
        syscall

        mov rcx, 0x40
        mov rsi, rsp
        mov rdi, buff
        rep movsb
        mov rsp, rbp
        pop rbp
        ret

mov rax, 0xf
syscall
ret

_start:
        jmp main


