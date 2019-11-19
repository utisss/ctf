#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int do_auth(char * pass);
void login();
void get_flag();

int main() {
  printf("I really like strings\n");
  login();
  return 1;
}

int do_auth(char * pass) {
  printf("I didn't like that one\n");
  return 0;
}

void login() {
  printf("Name your favorite string:\n");
  char buffer_123[100];
  gets(buffer_123);
  if(do_auth(buffer_123)) {
    get_flag();
  }
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
