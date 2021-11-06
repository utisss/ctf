#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

int main() {
  vuln();
  return 0;
}

void vuln() {
  char buffer[100];
  printf("Enter some input!\n");
  gets(buffer);
}

void get_flag(int x, int y) {
  if(x == 0xdeadbeef && y == 0xcafebabe) {
      char*  args[2] = {"/bin/sh", NULL};
      execve(args[0], args, NULL);
  }
}
