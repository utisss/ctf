#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

void get_flag();

int main() {
  char username[50];
  int8_t i = 0;
  
  printf("Only cool people can get the flag\n\n");
  
  getlogin_r(username, 50);
  printf("You are logged in as %s\n", username);
  
  if(strcmp(username, "huck") == 0) {
      printf("You're cool enough for the flag!\n");
      i = -1;
  }
  else {
      printf("You're not cool enough for the flag!\n");
  }

  int input = 1;
  do {
      if(input == 2 || input != 1) {
        return 0;
      }
      switch(i) {
        case -1:
            printf("Hey Huck! Here's a shell.\n");
            get_flag();
            break;
        case 0:
            printf("Hello! You're not cool enough for the flag, but I'll talk to you!\n");
            break;
        case 1:
            printf("Hey again! You're still not cool enough, but I have nothing better to do\n");
            break;
        case 2:
            printf("Hey. You're still not very cool...\n");
            break;
        case 3:
            printf("Why are you still here...?\n");
            break;
        case 4:
            printf("...\n");
            break;
        case 5:
            printf("I'm tired of you.\n");
            break;
        case 6:
            printf(">:(\n");
            break;
        default:
            printf("Go away.\n");
            break;
      }
      i++;
      printf("\n");
      printf("1: Keep talking\n");
      printf("2: Leave\n");

      printf("Enter input: ");
  } while(scanf("%d", &input));

  return 1;
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
