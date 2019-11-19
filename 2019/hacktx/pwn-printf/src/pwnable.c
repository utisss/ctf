#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  printf("All I want for christmas is a good string\n");
  printf("Pls give a good string\n");
  char buf[200];
  fgets(buf, 190, stdin);
  printf(buf);
  printf("\nthat was a pretty cool one\n");
  return 1;
}

void flag() {
  char* args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
