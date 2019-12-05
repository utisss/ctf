#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int do_auth(char * pass);
void login();
void get_flag();

int main() {
  char buf[200];
  printf("I really like strings\n");
  printf("Tell me your favorite string\n");
  gets(buf);
  printf("Good string\n");
  return 1;
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
