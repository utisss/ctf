#include <stdio.h>

int main() {
    char buf[30];
    char *ptr = buf;

    puts("Enter something: ");

    gets(buf);

    printf(buf);
}