#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void change(char* str, int sz) {
    for(int i = 0; i < sz; i++) {
        if(str[i] >= 'a' && str[i] <= 'z') {
            str[i] = (((str[i] - 'a') + 39) % 26) + 'a';
        }
    }
}

int main() {
    printf("What's the password lol?\n");
    printf("Enter a string:\n");
    char string[50];
    fgets(string, 50, stdin);
    change(string, 50);
    if(strcmp(string, "hgsynt{mbzchgre_mb_mrrc_mbbc}\n") == 0) {
        printf("Nice\n");
        exit(0);
    }
    printf("Wrong!\n");
}

