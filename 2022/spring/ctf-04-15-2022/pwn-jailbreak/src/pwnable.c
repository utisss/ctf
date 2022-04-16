#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

int main() {
    printf("What's your name?\n");
    char buffer[100];
    fgets(buffer, 100, stdin);
    printf("Hi ");
    printf(buffer);
    printf("\n");
    printf("Jailbreak needs your help! Send her a message to encourage her");
    char message[100];
    gets(message);
    return 0;
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
