#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

struct idk {
    int x;
    long long z;
};

int main() {
  int x = 0;
  printf("Struct on da stack fo today\n");
  struct idk overwriteme = {1, 23};
  char buffer[100];
  printf("Enter some input!\n");
  gets(buffer);
  if(overwriteme.x == 0x1337) {
    printf("How did I get here??\n");
    get_flag();
  }
  printf("Lol try again!\n");
  return 1;
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
