#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>

__attribute__((constructor))
static void __calloc() {
    if(ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        exit(1);
    }
}

char check[] = {83, 80, 66, 72, 127, 69, 89, 73, 15, 74, 64, 127, 125, 64, 78, 83, 74, 73, 125, 78, 74, 125, 71, 64, 73, 125, 85, 68, 127, 80, 125, 80, 12, 125, 76, 83, 80, 125, 68, 67, 78, 67, 91};

int main(int argc, char **argv) {
    char input[44];
    printf("Enter the flag:\n");
    fgets(input, 44, stdin);
    for(int i = 0; i < 43; ++i) {
        if(check[i] != ((input[i] - 3) ^ 33)) {
            printf("Wrong flag\n");
            return 1;
        }
    }
    printf("Correct flag\n");
    return 0;
}
