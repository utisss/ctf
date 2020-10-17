#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

unsigned int len = 200;
int main() {
  char buff[200];

  printf("Echo Server 2.0\nLength:\n");
  scanf("%u%*c", &len);
  printf("Input:\n");
  gets(explanation);
  write(1, explanation, len);
  return 1;
}

