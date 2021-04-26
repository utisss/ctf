#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  char* binsh = "/bin/sh";
  printf("%p\n",system);
  printf("%p\n",binsh);
  char buffer[100];
  printf("Enter some input!\n");
  gets(buffer);
  return 0;
}

