#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>



int main() {
    char** book = malloc(sizeof(char*)*10);
    for(int i=0;i<10;i++)
        book[i] = malloc(100);
    printf("Are you brave enough to read the Maleficarum? It has been known to drive men mad\n");
    while(1) {
        printf("0: Read a page\n");
        printf("1: Write on a page\n");
        printf("2: Destroy a page\n");
        printf("3: Repair a page\n");
        printf("4: Read the flag\n");
        int option = getc(stdin) - '0';
        getc(stdin);
        if(option == 0) {
            printf("Which page?\n");
            int page = getc(stdin) - '0';
            getc(stdin);
            if(page >= 0 && page < 10)
                for(int i=0;i<100;i++)
                    putc(book[page][i], stdout);
        }
        else if(option == 1) {
            printf("Which page?\n");
            int page = getc(stdin) - '0';
            getc(stdin);
            if(page >= 0 && page < 10) {
                fgets(book[page], 100, stdin);
            }
        }
        else if(option == 2) {
            printf("Which page?\n");
            int page = getc(stdin) - '0';
            getc(stdin);
            if(page >= 0 && page < 10 && book[page] != NULL) {
                free(book[page]);
                printf("You tear the page to shreds\n");
                book[page] = NULL;
            }
        }
        else if(option == 3) {
            printf("Which page?\n");
            int page = getc(stdin) - '0';
            getc(stdin);
            if(page >= 0 && page < 10 && book[page] == NULL) {
                book[page] = malloc(100);
                printf("You tape the torn up page back together\n");
            }
            else {
                printf("Page %d is not torn up!\n", page);
            }
        }
        else if(option == 4) {
            printf("You flip to the page with the flag\n");
            char* flag = malloc(100);
            FILE* flag_file = fopen("flag.txt", "r");
            fgets(flag, 100, flag_file);
            char* new_flag = malloc(100);
            sprintf(new_flag, "The flag, which is very important, is: %s", flag);
            printf("But the words on the page disappear as you try to read them\n"); 
            free(flag);
            free(new_flag);
        }
    }
}
