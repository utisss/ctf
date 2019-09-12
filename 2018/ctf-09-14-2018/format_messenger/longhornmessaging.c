#include <stdio.h>

//This looks really janky, but it's supposed to be like this to get the exploit to work.

void greet(char *profName, char *eid) {
    printf("\n Welcome, ");
    printf(eid);
    printf("\nPlease enter the message you would like to compose to %s:", profName);
}

int main(int argc, char **argv) {
    setbuf(stdout, NULL);
    printf("Welcome to the Longhorn Professor Messaging Service!\n Which Professor would you like to message?"); 
    
    char profName[20];
    char eid[20];
    char message[100];
    fflush(stdout);
    scanf("%20s", profName);

    setbuf(stdout, NULL);
    printf("\n Please enter your UT EID:");
    fflush(stdout);
    scanf("%20s", eid);
    greet(profName, eid);
        
    fflush(stdout);
    scanf("%300s", message);
    setbuf(stdout, NULL);
    printf("Sending message to %s\n", profName);
    return 0;
}
