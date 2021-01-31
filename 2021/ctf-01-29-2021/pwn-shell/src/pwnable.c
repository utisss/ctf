#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    char shellcode[500] = "";
    fgets(shellcode, 500, stdin);
    for(int i=0;i<500;i++) {
        char *blacklist = "/bin/sh";
        if(shellcode[i] != 0 && strchr(blacklist,shellcode[i]) != NULL) {
            puts("Blacklisted character found!");
            exit(-1);
        }
    }
    ((void(*)())shellcode)();
    return 0;
}
