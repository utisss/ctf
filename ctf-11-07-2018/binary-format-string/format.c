#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int defeatFormatString(char *str) {
    char count = 0;
    size_t len = strlen(str);
    for(int i = 0; i < len; ++i) {
        if(str[i] == '%') {
            ++count;
        }
    }
    if(count > 1) {
        printf("*teleports behind you* *slices through your format string attack* \"heh... not bad, you made me use 10 percent of my power\"");
        exit(1);
    }
}

void checkExit() {
    do {
        printf("Would you like to exit? y/n:\n");
        char res;
        scanf("%c%*c", &res);
        if(res == 'y') {
            printf("Exiting\n");
            exit(1);
        } else if(res == 'n') {
            return;
        }
    } while(1);
}

int main(int arc, char **argv) {
    setbuf(stdout, NULL);
    printf("Welcome to the echo server!\nPlease enter a string, and we'll echo it back to you: ");
    while(1) {
        setbuf(stdout, NULL);
        fflush(stdout);
        char buff[150];
        fgets(buff, 150, stdin);
        defeatFormatString(buff);
        printf(buff);
        checkExit();
        printf("Enter another string: ");
    }
}
