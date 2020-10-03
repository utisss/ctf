#include <stdio.h>

typedef void (*function)(void);
char flag[] = "utflag{x86_1s_deprec8ed}";

int main() {
    char buf[100];

    puts("Enter some shellcode: ");

    gets(buf);
    
    ((function)buf)();
}