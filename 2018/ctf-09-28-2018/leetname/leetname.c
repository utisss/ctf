#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * flag = "REDACTED";

void convert_to_leet(char * name, int length, char * output) {
  for (int i = 0; i < length; i++) {
    char letter = name[i];
    if (letter == 'o' || letter == 'O') {
      output[i] = '0';
    } else if (letter == 'e' || letter == 'E') {
      output[i] = '3';
    } else if (letter == 'l' || letter == 'L') {
      output[i] = '1';
    } else if (letter == 's' || letter == 'S') {
      output[i] = '5';
    } else if (letter == 'a' || letter == 'A') {
      output[i] = '4';
    } else if (letter == 't' || letter == 'T') {
      output[i] = '7';
    } else {
      output[i] = letter;
    }
  }
}

int main() {
  printf("Enter your name:\n");

  char * name = NULL;
  size_t len = 0;
  ssize_t read = getline(&name, &len, stdin);
  name[strlen(name) - 1] = '\0';

  int leetest_name_test = // REDACTED - some function of the name
  printf("Address is %p\n", (void *) &leetest_name_test);
  printf("Hello ");
  printf(name);
  printf("!\n");
  if (leetest_name_test == 1337) {
    printf("Your name qualifies as sufficiently leet!\n");
    printf("Here's your leet key: %s\n", flag);
  } else {
    char leet_name[strlen(name) + 1];
    convert_to_leet(name, strlen(name), leet_name);
    leet_name[strlen(name)] = '\0';
    printf("Your leet name is %s\n", leet_name);
    printf("Your name is not leet enough to gain access to our key.\n");
  }
}
