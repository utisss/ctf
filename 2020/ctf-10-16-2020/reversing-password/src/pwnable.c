#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    printf("What's the password lol?\n");
    printf("Enter a string:\n");
    char string[50];
    fgets(string, 50, stdin);
    if(strcmp(string, "utflag{password_lol}\n") == 0) {
        printf("Nice\n");
        exit(0);
    }
    printf("Wrong!\n");
}

