#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

unsigned char A000073(long long x);
char flag[] = {0x75, 0x25, 0x54, 0x13, 0x79, 0x76, 0xb9, 0xee, 0xae, 0xd5, 0xd1, 0xf8, 0xcb, 0xf3, 0xcd, 0x34, 0xf3, 0x40, 0xa7, 0xcc, 0x76, 0x52, 0x91, 0x34, 0x5f, 0x6d, 0x32, 0xf3, 0x5};

int main() {
    setbuf(stdout, NULL);
    printf("I hope you like sequences :)\n");
    printf("Here's the flag: ");
    for(int i = 0; i < 100; i++) {
        printf("%c", A000073(i*10) ^ flag[i]);
    }
}

unsigned char A000073(long long x) {
    if(x == 0) {
        return 0;
    }
    if(x == 1) {
        return 0;
    }
    if(x == 2) {
        return 1;
    }
    return A000073(x-1) + A000073(x-2) + A000073(x-3);
}
