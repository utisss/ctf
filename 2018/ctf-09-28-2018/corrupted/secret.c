#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>

__attribute__((constructor))
static void __calloc() {
    if(ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        printf("Don't trace me neckbeard\n");
        exit(1);
    }
}

char initial[] = { 88, 89, 75, 65, 116, 74, 94, 116, 109, 103, 5, 118, 109, 96, 27, 97, 92, 28, 6, 73, 6, 118, 88, 72, 122, 28, 4, 73, 109, 123, 76, 127, 102, 24, 79, 119, 7, 5, 91, 73, 7, 107, 5, 124, 7, 74, 2, 73, 79, 4, 78, 120, 125, 118, 5, 73, 95, 65, 125, 127, 4, 77, 79, 120, 100, 16, 16, 80};

int main(int argc, char **argv) {
    char output[68];
    for(int i = 0; i < sizeof(initial); ++i) {
        output[i] = (initial[i] ^ 41) + 4;
    }
    return 0;
}
