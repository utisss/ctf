#include <stdio.h>
#include <stdlib.h>

int main() {
    char results[10][20];
    char tmp[20];
    char *flag = "utflag{t00_many_files}";

    FILE *fp;

    for(int i = 0; i < 20; i++) {
        results[9][i] = 0;
    }

    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 20; j++) {
            results[i][j] = rand() % 256;
            results[9][j] ^= results[i][j];
        }
    }

    for(int i = 0; i <= strlen(flag); i++) {
        results[9][i] ^= flag[i];
    }


    for(int i = 0; i < 10; i++) {
        sprintf(tmp, "%d.txt", i);
        fp = fopen(tmp, "w");

        fwrite(results[i], 20, 1, fp);

        fclose(fp);
    }
}