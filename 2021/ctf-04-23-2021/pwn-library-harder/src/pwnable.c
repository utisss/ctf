#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  char buffer[100];
  puts("Enter some input!");
  gets(buffer);
  return 0;
}

