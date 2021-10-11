#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

int main() {
    puts("Enter a license key!");
    char buf[100];
    fgets(buf,100,stdin);
    char a=0;
    char b=0;
    char c=0;
    char d=0;
    for(int i=0;i<100;i+=4) {
        a += buf[i]-'0';
        b += buf[i+1]-'0';
        c += buf[i+2]-'0';
        d += buf[i+3]-'0';
    }
    if(!a && !b && !c && !d)
        get_flag();
    else
        printf("Invalid key");
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
