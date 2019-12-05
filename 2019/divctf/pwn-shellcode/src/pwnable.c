#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  char buf[500];
  printf("Give me some shellcode and I'll run it\n");
  fgets(buf, 500, stdin);
  ((int (*) ())buf)();
  return 1;
}
