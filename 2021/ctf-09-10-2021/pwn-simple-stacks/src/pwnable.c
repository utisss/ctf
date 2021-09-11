#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

char *rsp_str = "rsp";
char *rbp_str = "rbp";
char *ret_str = "ret";
char *blank_str = "   ";

void vuln() {
    printf("Stack before gets\n");
    register long *rsp asm("rsp");
    register long *rbp asm("rbp");
    printf("┌───────────────────────────────────────────┐\n");
    for(long *i = rbp+1; i>= rsp; i--) {
        char *str = NULL;
        if(i == rsp) {
            str = rsp_str;
        }
        else if(i == rbp) {
            str = rbp_str;
        }
        else if(i == rbp+1) {
            str = ret_str;
        }
        else {
            str = blank_str;
        }
        printf("│ % 3s │ %p │ %#18lx │\n",str,i,*i);
    }
    printf("└───────────────────────────────────────────┘\n");
    printf("Enter some data\n");
    char buffer[20];
    gets(buffer);
    printf("┌───────────────────────────────────────────┐\n");
    for(long *i = rbp+1; i>= rsp; i--) {
        char *str = NULL;
        if(i == rsp) {
            str = rsp_str;
        }
        else if(i == rbp) {
            str = rbp_str;
        }
        else if(i == rbp+1) {
            str = ret_str;
        }
        else {
            str = blank_str;
        }
        printf("│ % 3s │ %p │ %#18lx │\n",str,i,*i);
    }
    printf("└───────────────────────────────────────────┘\n");
}

int main() {
    vuln();
    return 0;
}

