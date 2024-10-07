#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>

void get_flag();

void rocket() {
  printf("Press enter to boost the rocket!\n");
  printf("           ___\n     |     | |\n    / \\    | |\n   |--o|===|-|\n   |---|   |d|\n  /     \\  |w|\n | U     | |b|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_\n");
  char buf[100];
  gets(buf);
  return;
}

int main() {
  pid_t p = fork(); 
  if(p<0){ 
    perror("fork fail"); 
    exit(1); 
  } 
  else if (p == 0) {
    while (true) {
      rocket();
    }
  }
  else {
    p = wait(NULL);
  }
  printf("Ok, here's your shell\n");
  get_flag();
}

void get_flag() {
  char*  args[2] = {"/bin/bash", NULL};
  execve(args[0], args, NULL);
}
