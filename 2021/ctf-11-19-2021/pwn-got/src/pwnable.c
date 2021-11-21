#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <math.h>

long *got_start = 0x404018;

void print_got() {
    printf("GOT:\n");
    printf("%s (%lx): %lx\n", "puts", got_start + 0, got_start[0]);
    printf("%s (%lx): %lx\n", "printf", got_start + 1, got_start[1]);
    printf("%s (%lx): %lx\n", "fgets", got_start + 2, got_start[2]);
    printf("%s (%lx): %lx\n", "scanf", got_start + 3, got_start[3]);
}

int main() {
    printf("Look at my GOT\n");
    print_got();
    printf("Let me call a function\n");
    char buf[100];
    fgets(buf, 100, stdin);
    printf("See how it changes\n");
    print_got();
    long index;
    long val;
    printf("Want to change one?\n");
    scanf("%ld", &index);
    scanf("%ld", &val);
    printf("GOT[%ld] = %lx\n", index, val);
    got_start[index] = val;
    puts(buf);
}

