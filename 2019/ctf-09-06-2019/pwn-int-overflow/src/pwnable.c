#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int do_auth(char * pass);
void login();
void get_flag();

int main() {
  printf("This is the Bapa Bohns raw socket delivery service.\n");
  printf("Only privileged users can order over TCP.\n");
  login();
  return 1;
}

void login() {
  int x = getuid(); // Get user id process caller

  char name[20];
  printf("Enter your name:\n");
  gets(name);

  if(x == 0) { // Check if we were called by root (user id = 0)
    printf("Access granted to %s", name);
    printf("What kind of bizza do you want.\n");
    get_flag();
  }
  else {
    printf("Warning! %s is an unprivileged user\n", name);
  }
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
