#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// https://gist.github.com/D0tty/e4712ab8024944f17533a1f5354ca83f

unsigned char extra[30000] = {0};
unsigned char tape[30000] = "utflag{huck_does_his_taxes_in_brainfuck}";

// set the pointer to point at the left-most cell of the tape
unsigned char* ptr = tape;

void interpret(char* input) {
    char current_char;
    size_t i;
    size_t loop;

    for (i = 0; input[i] != 0; i++) {
        current_char = input[i];
        if (current_char == '>') {
            ++ptr;
        } else if (current_char == '<') {
            --ptr;
        } else if (current_char == '+') {
            ++*ptr;
        } else if (current_char == '-') {
            --*ptr;
        } else if (current_char == '.' ) {
            putchar(*ptr);
        } else if (current_char == ',') {
            *ptr = getchar();
        } else if (current_char == '[') {
            continue;
        } else if (current_char == ']' && *ptr) {
            loop = 1;
            while (loop > 0) {
                current_char = input[--i];
                if (current_char == '[') {
                    loop--;
                } else if (current_char == ']') {
                    loop++;
                }
            }
        }
    }
}

int main() {
    char code[6];
    printf("Enter up to 5 bytes of code: ");
    scanf("%5s", code);

    interpret(code);
}