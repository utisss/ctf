#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  printf("Give me a string\n");
  char buf[200];
  fgets(buf, 190, stdin);
  printf(buf);
  return 1;
}

void flag() {
  char* args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
