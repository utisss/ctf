#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void caIIoc() {
    asm("movq %rax, %rdi");
}

void execCommand(char *command) {
    //OwO what is this?
    system(command);
}

char *specialEncrypt() {
    char plaintext[100];
    fflush(stdout);
    gets(plaintext);
    char *cipherText = malloc(100);
    size_t length = strlen(plaintext);
    for(int i = 0; i < length; ++i) {
        cipherText[i] = plaintext[i] ^ 0x41;
    }
    return cipherText;
}

int main(int argc, char **argv) {
    setbuf(stdout, NULL);
    printf("Welcome to the Longhorn Encryption Service!\nPlease enter a string for us to encrypt:");
    char *cipherText = specialEncrypt();
    setbuf(stdout, NULL);
    printf("Here is your encrypted message: %s\n", cipherText);
    return 0;
}
