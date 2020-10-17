#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int stage1();
int stage2();
int stage3();

int main() {
  int x = 0;
  printf("Hi!\n");
  printf("I'm a bomb!\n");
  printf("Hopefully you don't blow me up!\n");

  if(!stage1()) {
      printf("BOOM!\n");
      exit(0);
  }
  if(!stage2()) {
      printf("BOOM!\n");
      exit(0);
  }
  if(!stage3()) {
      printf("BOOM!\n");
      exit(0);
  }

  // Open file 
  FILE *fptr;
  char c;
  fptr = fopen("flag.txt", "r"); 
  if (fptr == NULL) 
  { 
    printf("Cannot open file \n"); 
    exit(0); 
  } 

  // Read contents from file 
  c = fgetc(fptr); 
  while (c != EOF) 
  { 
    printf ("%c", c); 
    c = fgetc(fptr); 
  } 

  fclose(fptr); 
  return 1;
}

int stage1() {
    int x, y;
    scanf("%d %d", &x, &y);
    if(x + y == 420) {
        printf("Stage 1 disarmed\n");
        return 1;
    }
    return 0;
}

int stage2() {
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);
    if(z * (x + y) == 69) {
        printf("Stage 2 disarmed\n");
        return 1;
    }
    return 0;
}

int stage3() {
    int x, y;
    scanf("%d %d", &x, &y);
    if(x << y == 64) {
        printf("Stage 3 disarmed\n");
        return 1;
    }
    return 0;
}

void get_flag() {
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
