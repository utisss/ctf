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

unsigned char store[] = {103, 50, 227, 77, 215, 218, 202, 221, 1, 222, 5, 18, 254, 70, 242, 39, 27, 152, 8, 100, 173, 9, 28, 120, 144, 216, 2, 241, 97, 140, 220};

unsigned char pad[] = {18, 70, 133, 33, 182, 189, 177, 148, 94, 159, 72, 77, 173, 119, 159, 87, 119, 169, 107, 85, 157, 86, 68, 60, 200, 156, 90, 181, 57, 200, 161};

int main(int argc, char **argv) {
    printf("Please Login: \n");
    char pass[35];
    fgets(pass, 35, stdin);
    for(int i = 0;i < sizeof(store) ; ++i) {
        if(store[i] != (pass[i] ^ pad[i])) {
            printf("Wrong password\n");
            return 1;
        }
    }
    printf("Correct password\n");
    return 0;
}
