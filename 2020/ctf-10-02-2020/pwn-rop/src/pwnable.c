#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// Idk I'm just gonna leave this here
char binsh_string[8] = "/bin/sh";

int main() {
  int x = 0;
  printf("Red sus\n");
  printf("What was your last task?\n");
  char buffer[100];
  gets(buffer);
  printf("Red is the imposter\n");
  return 1;
}

// Force system() into PLT
void func() {
    // This will crash
    system(0);
}
