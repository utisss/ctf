#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>

void ping(char * IP){
    char command[64];
    strcpy(command,"ping -c 5");
    command[9] = 32;
    strcpy(command+10,IP);
    system(command);
}

int main() {
    printf("Welcome to ping shell. You are only allowed to ping\n");
    printf("Recognized commands: ping\n");
    char commandBuf[64];
    while(1){
        printf("shell> ");
        fgets(commandBuf, 64, stdin);
        char sub[64];
        strncpy(sub, commandBuf+5, 40);
        if (strncmp(commandBuf,"ping",4)!=0 || strchr(commandBuf, '$')||strchr(commandBuf, '&')||strchr(commandBuf, '|')||strchr(commandBuf, '`')){
            printf("invalid command. please dont hack me.");
            exit(1);
        }
        ping(sub);
    }

    return 0;
}
