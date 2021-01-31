#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


void get_response() {
    char buffer[0x100];
    fgets(buffer, 0x100, stdin);
    printf(buffer);
    printf(" to the moon!");
}

int main() {
    printf("Which stock do we like?\n");
    get_response();
    exit(0);
}

