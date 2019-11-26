#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#define LEN 78

__attribute__((constructor))
static void __calloc() {
    if(ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        exit(1);
    }
}

char check[] = {64, 65, 87, 89, 108, 86, 74, 89, 28, 66, 65, 80, 95, 110, 90, 28, 81, 110, 70, 2, 110, 81, 29, 95, 22, 65, 110, 85, 108, 71, 2, 110, 88, 64, 82, 85, 110, 65, 28, 88, 2, 110, 93, 2, 2, 110, 84, 66, 110, 108, 82, 65, 64, 108, 89, 89, 68, 110, 66, 65, 94, 67, 80, 81, 110, 84, 95, 110, 65, 85, 80, 110, 31, 31, 31, 31, 72};
int main(int argc, char **argv) {
    char input[LEN];
    printf("What's the secret that caused the pilgrims to flee Britain?:\n");
    fgets(input, LEN, stdin);
    for(int i = 0; i < LEN-1; ++i) {
        if(check[i] != ((input[i] - 2) ^ 0x33)) {
            printf("I don't think that's right...\n");
            return 1;
        }
    }
    printf("Fascinating\n");
    return 0;
}
