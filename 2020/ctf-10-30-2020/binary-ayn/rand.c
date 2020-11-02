#include <stdio.h>
#include <stdlib.h>

int main() {
    srand(time(NULL));
    
    int guess;
    int secret = rand();

    printf("What number am I thinking of? ");
    scanf("%d", &guess);

    if(guess != secret) {
        printf("No, the secret was %d\n", secret);
    }else{
        printf("Wow, how did you get that?\n");
        system("/bin/sh");
    }
}