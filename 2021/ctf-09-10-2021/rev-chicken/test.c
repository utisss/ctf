#include <stdio.h>
#include <stdbool.h>

char flag[] = {28, 16, 13, 66, 8, 3, 16, 77, 1, 85, 8, 69, 90, 10, 52, 74, 89, 87, 24, 113, 30, 12, 95, 90, 54, 7, 3, 31, 10, 15, 88, 64, 54, 20, 7, 29, 8, 81, 14, 27, 20}; 

int main() {
    char x[5];
    puts("Why did the chicken cross the road?");
    fgets(x, 5, stdin);
    for(unsigned int i = 0; i < 41; i++)
        flag[i] ^= x[i % 4];
    puts(flag);
    return 0;
}
