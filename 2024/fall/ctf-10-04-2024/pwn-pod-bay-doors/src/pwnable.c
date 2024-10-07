#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
  printf("Affirmative, Dave. I read you.\n");
  printf("1) Print flag\n");
  printf("2) Send a message\n");
  printf("3) Exit\n");
  char inp[3];
  fgets(inp, 3, stdin);
  if (inp[0] == '1') {
    printf("I'm sorry Dave. I'm afraid I can't do that.\n");
    exit(1);
  } else if (inp[0] != '2') {
    exit(1);
  }
  char buffer[256];
  printf("Type your message here (max 256 characters)\n");
  gets(buffer);
  printf("You said: ");
  printf(buffer);
  return 1;
}

void get_flag() {
  FILE* file = fopen("flag.txt", "r");
  char flag[256];
  fgets(flag, 256, file);
  printf("%s\n",flag);
}
