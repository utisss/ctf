#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void login(int *login);
void get_flag();

int main() {
  int *n = malloc(sizeof(int));
  *n = 0xdead;
  login(n);
  return 1;
}

void login(int *login) {
  printf("Welcome to Turkey's First Login Portal! You may supply a format string to examine the login value (i.e. \"login ptr: %%p, login val: %%x\"):\n");
  char str[100];
  fgets(str, 100, stdin);
  printf(str, login, *login);
  printf("%x\n", *login);
  if (*login == 0x1337) {
    get_flag();
  }
  else {
    printf("Sorry, login value was invalid. Gobble gobble!");
  }
}

void get_flag() {
  printf("You better not steal my stuffing!");
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
