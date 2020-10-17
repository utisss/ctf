#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    char echo[0x50];
    puts("Echo Server Version 1.0\nInput:\n");
    fgets(echo, 0x50, stdin);
    printf(echo);
    exit(0);
}

