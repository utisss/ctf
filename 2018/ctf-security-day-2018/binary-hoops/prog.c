#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int safeuphere = 0;

void print_flag() {
    system("cat flag.txt");
}

void run() {
    char answer[100];
    scanf("%s", answer);
}

int main(int argc, char **argv) {

    int* ptr = &safeuphere;
    printf(argv[1]);

    if(safeuphere == 420) {
        run();
    }

    return 0;
}
