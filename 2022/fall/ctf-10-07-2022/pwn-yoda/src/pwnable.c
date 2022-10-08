#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char input[1024];

void get_flag() {
    char* args[2] = {"/bin/sh", NULL};
    execve(args[0], args, NULL);
}

void reverse(char *input, char *output, int len) {
    for (int i = 0; i < len; i++) {
        output[i] = input[len - i - 1];
    }
    output[len] = '\0';
}

int main() {
    char output[32];
    int len = -1;

    memset(input, 0, sizeof(input));

    puts("Reverse your string, I will.");
    puts("How long is your string?");
    fgets(input, sizeof(input), stdin);
    sscanf(input, "%d", &len);
    if (len < 0 || len > sizeof(input) - 1) {
        puts("Much too long, that string is. Control, control, you must learn control.");
        return 1;
    }
    puts("What is your string?");
    fgets(input, len+1, stdin);

    reverse(input, output, len);

    puts("Here is your string:");
    puts(output);

    return 0;
}
