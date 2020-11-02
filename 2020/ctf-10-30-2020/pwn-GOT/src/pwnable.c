#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

int main() {
    uint64_t addr = 0;
    uint64_t val = 0;

    puts("I will allow you overwrite one address with any value\n");

    printf("Enter the address in hex:\n");
    // Read a 64-bit hex number from stdin
    scanf("%llx", &addr);

    printf("Enter the value in hex:\n");
    // Read a 64-bit hex number from stdin
    scanf("%llx", &val);

    // Overwrite the memory at addr to val
    *((uint64_t *)addr) = val;

    puts("Well, that didn't work...\n");

    return 1;
}

void get_shell() {
    system("/bin/sh");
}
