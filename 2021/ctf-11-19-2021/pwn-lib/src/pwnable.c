#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

char *binsh = "/bin/sh";

void vuln() {
    printf("uwu what's this %lx?\n", system);
    char buffer[100];
    gets(buffer);
}

int main() {
    vuln();
    return 0;
}

