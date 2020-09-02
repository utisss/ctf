#include <stdio.h>
#include <stdlib.h>

char str[] = {55,54,36,46,35,37,57,55,32,55,44,54,55,29,43,49,29,38,39,50,48,39,33,35,54,39,38,63,0x42};
int main() {
    char input[sizeof(str)];
    printf("What's the flag? ");
    fgets(input, sizeof(str), stdin);

    for(int i = 0; i < sizeof(str); i++) {
        if((input[i] ^ 0x42) != str[i]) {
            printf("Try again!\n");
            exit(0);
        }
    }

    printf("You got it!\n");
}