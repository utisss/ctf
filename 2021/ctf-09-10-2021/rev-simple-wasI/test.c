#include <stdio.h>

unsigned char flag[] = {231, 208, 142, 24, 27, 165, 113, 21, 27, 185, 47, 237, 50, 27, 96, 237, 27, 96, 188, 249, 226, 226, 159};

void encrypt(unsigned char input[24]) {
    for(int i = 0; i < 23; i++) {
        input[i] = input[i] * 23 + 100;
    }
}

int main() {
    unsigned char input[24];

    printf("Enter the flag: \n");
    scanf("%23s", input);
    
    encrypt(input);

    for(int i = 0; i < 23; i++) {
        if(input[i] != flag[i]) {
            printf("Wrong!\n");
            return 1;
        }
    }

    printf("Correct!\n");
}