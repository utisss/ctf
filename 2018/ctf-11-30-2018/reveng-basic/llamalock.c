#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char * a = NULL;  
    unsigned long n;
    int len = getline(&a, &n, stdin) - 1;
    puts(a);

    for (int i = 0; i < len; i++) {
        a[i] = a[i] + 3;
    }

    char * b = malloc(sizeof(char) * (len));
    for (int i = 0; i < len; i++) {
        b[len - i - 1] = a[i];
    }

    for (int i = 0; i < len; i++) {
        b[i] = b[i] - 5;
    }

    char * desired = "{b1r2pp1t.]1p2]3lser.fq]j2a/ra2rye_jdrs";
    if (strcmp(b, desired) == 0) {
        printf("%s\n", "Congratulations! Take your loot. The flag is the code you entered.");
    } else {
        printf("%s\n", "BZZT. BZZT. BZZT. INCORRECT.");
    }
    
    free(a);
    free(b);
    return 0;
}
