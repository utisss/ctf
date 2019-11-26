#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  printf("I am thankful for format string vulnerabilities\n");
  char buf[200];
  fgets(buf, 190, stdin);
  printf(buf);
  printf("\nthat was a pretty cool one\n");
  return 1;
}

void flag(int *x) {
  if(*x != 0x1337) {
    return;
  }
  char* args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
