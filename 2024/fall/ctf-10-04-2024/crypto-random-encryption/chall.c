#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE* file = fopen("flag.txt", "r");
    char flag[256];
    fgets(flag, 256, file);
    int pos = 0;
    while (flag[pos]) {
        printf("0x%02X ", (rand() % 256) ^ flag[pos++]);
    }
    printf("\n");
}