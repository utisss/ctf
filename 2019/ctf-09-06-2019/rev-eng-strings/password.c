#include <stdio.h>
#include <string.h>

int main() {
  printf("What's the password >:)\n");
  char password[50];
  fgets(password, 50, stdin);
  if(strcmp(password, "utflag{h4rdc0d3d_str1ngs}\n") == 0)
    printf("Aw you guessed it :(\n");
  else
    printf("Haha I knew you didn't know it\n");
}
