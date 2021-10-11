#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

void vuln() {
    char buf[100];
    gets(buf);
}

int main() {
    puts("Where did I leave puts again?");
    void *location;
    scanf("%ld\n",&location);
    if(location == puts)
        get_flag();
    else
        vuln();
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
