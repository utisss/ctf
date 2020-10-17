#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

char password[16] = {99, 65, 74, 43, 35, -42, -122, 10, 21, 38, 71, 25, 74, 127, 120, 0};

void decrypt(char *array, int array_size);

int main() {
    printf("What's the password lol?\n");
    printf("Enter a string:\n");
    char string[16];
    fgets(string, 16, stdin);
    decrypt(password, 16);
    if(strcmp(string, password) == 0) {
        printf("Nice\n");
        exit(0);
    }
    printf("Wrong!\n");
}

void decrypt(char *array, int array_size)
{
    int i;
    char secret[16] = { 22, 53, 44, 71, 66, 177, 253, 122, 122, 65, 32, 124, 56, 12, 5, 0 };
    for(i = 0; i < array_size; i++)
        array[i] ^= secret[i];
}
