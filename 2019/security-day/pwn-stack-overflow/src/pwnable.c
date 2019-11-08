#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void login();
void get_flag();

int main() {
  printf("i like strings\n");
  printf("give me a cool one\n");
  login();
  printf("that was a good one\n");
  return 1;
}

void login() {
  char buffer_123[50];
  gets(buffer_123);
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
