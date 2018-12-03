#include <stdio.h>
#include <stdlib.h>

void owo(char *command) {
    system(command);
}

void welcome_vbucks_buyer(char *name) {
    printf("Greetings, %s (John Wick)!\n", name);
}

void welcome_normie(char *name) {
    printf("Welcome %s...AKA NO-SKINNER", name);
}
struct welcome {
    void (*welcome_function)(char *name);
};

int main(int argc, char **argv) {
    setbuf(stdout, NULL);
    fflush(stdout);
    printf("*** Welcome to Fortnite! ***\n");
    char *name = malloc(16);
    struct welcome *welFunc = malloc(sizeof(struct welcome));
    printf("Do you want to buy vbucks? y/n:\n");

    char member;
    scanf("%c%*c", &member);
    if(member == 'y') {
        welFunc->welcome_function = &welcome_vbucks_buyer; 
    } else if(member == 'n') {
        welFunc->welcome_function = &welcome_normie;
    } else {
        printf("Someone can't follow instructions\n");
        return 0;
    }
    free(welFunc);
    if(member == 'y') {
        printf("*** Please enter how many vbucks you want to buy: \n");
        char *vbucks = malloc(8);
        gets(vbucks);
    }
    printf("*** Please enter your username(Max 16 characters: \n");
    fgets(name, 16, stdin);
    welFunc->welcome_function(name);
    free(name);
    return 0;
}
