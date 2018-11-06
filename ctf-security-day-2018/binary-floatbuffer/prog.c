#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void print_flag() {
    system("cat flag.txt");
}


void run(char *input) {

    char buf[16];
    double nothing = 0.0f;
    strcpy(buf, input);


    if (nothing == 493.2) {
        print_flag();
    } else {
        printf("nothing is %f\n", nothing);
    }

}


int main(int argc, char** argv) {
    if(argc > 1) {
        run(argv[1]);
    }

    return 0;
}

