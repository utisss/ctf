#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char buf[18];
  puts("What's the password? ");
  scanf("%17s", buf);

  if (strcmp(buf, "spoOoOky-password") == 0) {
    char flag[64];
    FILE *fp = fopen("/flag.txt", "r");
    if (fp != NULL) {
      fread(flag, sizeof(char), 64, fp);
      fclose(fp);
      printf("Welcome to the graveyard!\n%s\n", flag);
    } else {
      printf("Hmm, can't find /flag.txt on this computer!\n");
    }
  } else {
    printf("Sorry, looks like you're not spooky enough to enter.\n");
  }
}
