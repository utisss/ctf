#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int do_auth(char * pass);
void login();
void get_flag();

int main() {
  printf("Welcome to the Bepis remote access database.\n");
  login();
  return 1;
}

int do_auth(char * pass) {
  printf("Authentication not implemented yet, come back later.\n");
  return 0;
}

void login() {
  printf("Enter password:\n");
  char buffer_123[30];
  gets(buffer_123);
  if(do_auth(buffer_123)) {
    get_flag();
  }
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
