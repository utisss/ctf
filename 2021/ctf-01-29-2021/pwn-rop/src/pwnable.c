#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_shell();

int main() {
  int x = 0;
  printf("Give me a cool string!\n");
  char buffer[256];
  printf("Enter some input!\n");
  gets(buffer);
  printf("That string wasn't very cool!\n");
  return 1;
}

void get_shell(int x) {
  char*  args[2] = {"/bin/sh", NULL};
  if(x == 0x1337)
      execve(args[0], args, NULL);
}
