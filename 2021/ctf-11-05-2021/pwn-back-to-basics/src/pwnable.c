#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

int main() {
    vuln();
    return 0;
}

void vuln() {
  printf("I really hope no one gets to my secret function located at %p\n", get_flag);
  char buffer[100];
  printf("Enter some input!\n");
  gets(buffer);
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
