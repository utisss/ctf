BITS 64

section .bss
input resb 60

; strlen = 59
section .data
greetings db 'Enter the flag', 0xa
greetings_len equ $ - greetings

congrats db 'Correct', 0xa
congrats_len equ $ - congrats

failed db 'Incorrect', 0xa
failed_len equ $ - failed

key db 54, 67, 187, 62, 127, 202, 15, 140, 8, 254, 148, 71, 147, 79, 141, 16, 245, 119, 190, 2, 195, 1, 206, 2, 31, 77, 223, 25, 217, 218, 120, 76, 177, 250, 174, 38, 205, 118, 190, 237, 63, 78, 31, 112, 186, 108, 97, 49, 103, 49, 123, 236, 108, 3, 198, 136, 8, 193, 234
stack:
	dq junk
	dq 0x3
	db 13, 34, 32

	dq antidebug

	dq junk
	dq 0x4
	db 40, 34, 10, 3

	dq write
	dq greetings
	dq greetings_len
	dq read
	dq input
	dq 60

	dq junk
	dq 0x8
	dq 0x40078


	dq pop_rsi
	dq key

	dq pop_rdi
	dq input

		
;put shit here

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x43
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x37
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xdd
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x52
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x1e
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xad
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x74
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xc5
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x57
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x9f
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xd9
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x18
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xe5
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x2a
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xdf
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x69
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xaa
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x4
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xeb
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x72
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xb1
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x30
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xbd
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x67
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x7b
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x12
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xab
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x71
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xb8
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xae
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x27
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x3f
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x81
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x97
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x9d
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x16
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xa3
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x13
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xe1
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x9e
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xf
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x7f
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x69
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x15
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xde
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x33
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x15
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x59
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x56
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x42
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x24
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x8b
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x6
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x5c
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xa8
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xed
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x7a
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0xa5
	dq check
	dq inc_rsi
	dq inc_rdi

	dq deref_rsi_rax
	dq deref_rdi_rbx
	dq xor_rbx
	dq 0x97
	dq check
	dq inc_rsi
	dq inc_rdi

	dq write
	dq congrats
	dq congrats_len
	dq finish

section .text
global _start

_start:
	mov rcx, stack
	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx


push_rbx:

	mov r8, [rcx]
	lea rcx, [rcx + 8]
	
	lea rcx, [rcx - 8]
	mov [rcx], rbx
	
	jmp r8


deref_rsi_rax:
	mov ah, byte [rsi]
	jmp act_fini


deref_rdi_rbx:
	mov bh, byte [rdi]
	jmp act_fini

xor_rbx:
	mov dh, byte [rcx]
	lea rcx, [rcx + 8]
	
	xor bh, dh

	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx

inc_rsi:
	inc rsi
	jmp act_fini

inc_rdi:
	inc rdi
	jmp act_fini

pop_rdi:
	mov rdi, [rcx]
	lea rcx, [rcx + 8]

	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx

pop_rsi:
	mov rsi, [rcx]
	lea rcx, [rcx + 8]

	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx

check:
	;mov rax, [rcx]
	;lea rcx, [rcx + 8]

	;mov rsi, [rcx]
	;lea rcx, [rcx + 8]

	sub bh, ah
	je gucci
	jmp exit_bad
gucci:
	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx

write:
	mov rsi, [rcx]
	lea rcx, [rcx + 8]
	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	mov rdi, 0x1
	mov rax, 1

	push rcx
	syscall
	pop rcx

	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx

read:
	mov rsi, [rcx]
	lea rcx, [rcx + 8]
	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	mov rdi, 0
	mov rax, 0

	push rcx
	syscall
	pop rcx
	
	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx

exit_bad:
	
	lea rcx, [rcx - 8]
	mov qword [rcx], finish

	lea rcx, [rcx - 8]
	mov qword [rcx], failed_len	

	lea rcx, [rcx - 8]	
	mov qword [rcx], failed 

	jmp write	
finish:
	mov rax, 60
	mov rdi, 1
	syscall


act_fini:
	mov rdx, [rcx]
	lea rcx, [rcx + 8]
	jmp rdx

antidebug:
	push rcx
	mov rdi, 0
	mov rsi, 0
	mov rdx, 1
	mov r10, 0
	mov rax, 101
	syscall
	mov rbx, 0xFFFFFFFFFFFFFFFF
	cmp rax, rbx
	jne good
	jmp finish
good:
	pop rcx
	jmp act_fini

	
junk:
	mov r10, [rcx]
	lea rcx, [rcx + 8]
	add rcx, r10
	jmp act_fini


