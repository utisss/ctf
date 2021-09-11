#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

void vuln() {
    unsigned int i = 0;
    char name[20];

    printf("What's your name? ");

    scanf("%100s", name);

    printf("Hello, %s\n", name);

    if(i == 0xdeadbeef) {
        get_flag();
    }
}

int main() {
    vuln();
    return 0;
}

