#include <stdio.h>
#include <stdlib.h>

char buff[50];

int main(int arc, char **argv) {
    printf("Will is thiccccc\n");
    fgets(buff, 50, stdin);
    printf(buff);
    exit(0);
}
