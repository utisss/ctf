#include <stdio.h>
#include <stdlib.h>

void owo(char *command) {
    system(command);
}

void welcome_normie(char *name) {
    printf("Watch this, %s: https://www.youtube.com/watch?v=cFZTAm2Jxq0\n", name);
}

void welcome_ninja_subscriber(char *name) {
    printf("Hey %s. Thanks for the subscribe bro", name);
}
struct welcome {
    void (*welcome_function)(char *name);
};

int main(int argc, char **argv) {
    char *name = malloc(35);
    struct welcome *welFunc = malloc(sizeof(struct welcome));
    setbuf(stdout, NULL);
    fflush(stdout);
    printf("Do you want to subscribe to ninja? y/n:\n");
    char member;
    scanf("%c%*c", &member);
    if(member == 'y') {
        welFunc->welcome_function = &welcome_ninja_subscriber; 
    } else if(member == 'n') {
        welFunc->welcome_function = &welcome_normie;
    } else {
        printf("Someone can't follow instructions\n");
        return 0;
    }
    printf("***Please enter your name: \n");
    fgets(name, 0x55, stdin);
    welFunc->welcome_function(name);
    free(name);
    free(welFunc);
    return 0;
}
