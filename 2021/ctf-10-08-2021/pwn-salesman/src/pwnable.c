#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int flag1 = 0;
int flag2 = 0;
int flag3 = 0;

void jump1() {
    flag1 = 1;
}

void jump2() {
    if(flag1) flag2 = 1;
}

void jump3() {
    if(flag2) flag3 = 1;
}

void get_flag() {
    if(flag3) {
        char*  args[2] = {"/bin/sh", NULL};
        execve(args[0], args, NULL);
    }
}


int main() {
    char buf[100];
    gets(buf);
}

