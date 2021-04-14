#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void get_flag();

int main() {
  char buffer[100];
  gets(buffer);
}

void get_flag(int x, int y) {
    if(x == 1 && y == 2) {
      char*  args[2] = {"/bin/sh", NULL};
      execve(args[0], args, NULL);
    }
}
