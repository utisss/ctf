#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
  int seed = 0;
  printf("%s", "Enter latest random number/current seed: \n");
  int n = scanf("%d", &seed);
  if (n != 1) {
    printf("%s", "A number, silly.\n");
    return -1;
  }
  initstate(seed, malloc(8), 8);
  printf("%d\n", rand());
}
