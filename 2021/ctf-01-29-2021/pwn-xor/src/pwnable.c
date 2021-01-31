#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

int main() {
    int len = 0;
    printf("%d\n",len);
    char buf[100];
    puts("Welcome to XOR as a service!");
    puts("Give me the length of your input");
    scanf("%d", &len);
    getchar();
    printf("Thanks! Now give me an input of length %d\n", len);
    (fgets)(buf,len,stdin);
    puts("xor time!");
    for(int i=0;i<len;i++) {
        buf[i] ^= 13;
    }
    puts("here you go");
    puts(buf);
    return 0;
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
