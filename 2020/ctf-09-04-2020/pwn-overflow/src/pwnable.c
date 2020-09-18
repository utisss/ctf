#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

int main() {
  int x = 0;
  printf("There's no way x will ever be 0x1337!\n");
  printf("My friend told me that gets was unsafe, but I don't care!\n");
  char buffer[100];
  printf("Enter some input!\n");
  gets(buffer);
  if(x == 0x1337) {
    printf("How did I get here??\n");
    get_flag();
  }
  printf("I knew gets was safe!\n");
  return 1;
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
