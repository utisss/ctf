#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  printf("i really like printing strings\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("eeeeeeee\n");
  printf("do you have any fun strings?\n");
  char buf[200];
  fgets(buf, 190, stdin);
  printf(buf);
  printf("\nthat was a pretty cool one\n");
  return 1;
}

void flag() {
  char* args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
