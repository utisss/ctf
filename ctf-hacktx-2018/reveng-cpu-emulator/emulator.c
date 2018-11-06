#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <sys/ptrace.h>

#define MAX_INSTRUCTIONS 100
#define INSTRUCTION_SIZE 3
#define OPERAND_SIZE 4

uint32_t regs[5];
uint32_t ip;
int8_t cmp_reg;
int end = 0;

struct operation {
    uint32_t op;
    uint32_t lhs;
    uint32_t rhs;
};

__attribute__((constructor))
static void antidebug() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        printf("Quit debugging me, you dirty neckbeard!\n");
        exit(1);
    }
}

uint8_t mem[500];

uint8_t strings[300];

uint32_t instructions[MAX_INSTRUCTIONS * INSTRUCTION_SIZE];

void parseOp(struct operation *curr) {
    int op = curr->op;
    int lhs = curr->lhs;
    int rhs = curr->rhs;
//    printf("Op: 0x%x\n", op);
    if(op == 0x41) {
        //XOR
        regs[lhs] ^= rhs;
    } else if(op == 0x67) {
        //AND
        regs[lhs] &= rhs;
    } else if(op == 0x23) {
        //OR
        regs[lhs] |= rhs;
    } else if(op == 0x34) {
        //ADD
        regs[lhs] += rhs;
    } else if(op == 0x89) {
        //SUBTRACT
        regs[lhs] -= rhs;
    } else if(op == 0x98) {
        //MOVE REG TO MEM
        //printf("0x%x\n", regs[rhs]);
        mem[regs[lhs]] = regs[rhs];
    } else if(op == 0x99) {
        //MOVE MEM TO REG
        regs[lhs] = mem[regs[rhs]];
    } else if(op == 0x55) {
        //CMP
        cmp_reg = regs[lhs] - rhs;
        //printf("%d\n", regs[lhs]);
    } else if(op == 0x56) {
        //JMP NOT EQUALS
        ip = cmp_reg != 0 ? lhs : ip;
        
    } else if(op == 0x57) {
        //JMP EQUALS
        ip = cmp_reg == 0 ? lhs : ip;
    } else if(op == 0x61) {
        //strcmp
        cmp_reg = strcmp(mem + lhs, strings + rhs);
    } else if(op == 0x21) {
        //printf
        printf("%s", strings + lhs);
    } else if(op == 0x22) {
        fgets(strings + lhs, rhs, stdin);
    } else if(op == 0x5) {
        regs[lhs] = strings[regs[rhs]];
    } else if(op == 0x14) {
        regs[lhs] ^= regs[rhs];
    } else if(op == 0x93) {
        //unconditional jump
        ip = lhs - 3;
    } else {
        end = 1;
    }
}

int main(int argc, char **argv) {
    if(argc < 2 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
        printf("Usage: ./emulator <filename.ROM>\n");
        return 0;
    }

    FILE *rom = fopen(argv[1], "r");
    
    //Read information from executable
    fread(instructions, OPERAND_SIZE, MAX_INSTRUCTIONS * INSTRUCTION_SIZE, rom);
    fread(strings, 1, 300, rom);
    //printf("%s\n", strings + 58);

    while(!end) {
        struct operation curr;
        curr.op = instructions[ip];
        curr.lhs = instructions[ip + 1];
        curr.rhs = instructions[ip + 2];
        parseOp(&curr);
        ip += 3;
    }
	return 0;
}
