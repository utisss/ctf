#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  printf("%s\n", "I am thankful for buffer overflows");
  printf("%s\n", "I bet no one solves this problem :)");
  char buf[200];
  printf("Thanks for the %d bytes", strlen(buf));
  gets(buf);
  puts(buf);
  return 1;
}
