#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

void get_input() {
    char dat[100];
    fgets(dat,100,stdin);
    puts(dat);
}

void check_pass() {
    char password[50];
    char favorite_number[4];
    if(strcmp(password, "super_secret_password") == 0 && *(int *) favorite_number == 42069) {
        puts("haha funny number");
        get_flag();
    }
    else {
        puts("better luck next time");
    }
}

int main() {
    get_input();
    check_pass();
    return 0;
}

