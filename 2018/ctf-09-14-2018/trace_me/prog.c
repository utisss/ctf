#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

char * passwordFileName = "pass.txt";
char * flagFileName = "flag.txt";

int passwordLen = 26;

int flagLen = 29;

char * OTP = "badtypeoffishpleasedisregard";

char * encrypt(char * passwd, int length) {
        int OTPlength = strlen(OTP);
        char * encrypted = (char *) malloc(sizeof(char) * (length + 1));
        for (int i = 0; i < length; i++) {
                encrypted[i] = 24 + (passwd[i] ^ OTP[i % OTPlength]);
        }
        encrypted[length] = 0;
        return encrypted;
}

char * decrypt(char * encrypted, int length) {
        int OTPlength = strlen(OTP);
        char * decrypted = (char *) malloc(sizeof(char) * (length + 1));
        for (int i = 0; i < length; i++) {
                decrypted[i] = (encrypted[i] - 24) ^ OTP[i % OTPlength];
        }

        decrypted[length] = 0;
        return decrypted;

}

int main() {
        /*// PROBLEM SETUP
        char * password = "s3cur1ty_thr0ugh_0b5cur1ty";
        char * flag = "utflag{ltrace_1s_y0ur_fr13nd}";

        FILE * passFile = fopen(passwordFileName, "w");
        fputs(encrypt(password, passwordLen), passFile);
        fclose(passFile);

        FILE * flagFile = fopen(flagFileName, "w");
        fputs(encrypt(flag, flagLen), flagFile);
        fclose(flagFile);*/

        char passBuf[50];
        FILE * passFile = fopen(passwordFileName, "r");
        fgets(passBuf, 50, passFile);

        char flagBuf[50];
        FILE * flagFile = fopen(flagFileName, "r");
        fgets(flagBuf, 50, flagFile);

        printf("Enter the password:\n");
        char line[LINE_MAX];
        if (fgets(line, LINE_MAX, stdin) != NULL) {
                if (strncmp(line, decrypt(passBuf, passwordLen), passwordLen) == 0) {
                        printf("Congratulations! Your flag is %s\n", decrypt(flagBuf, flagLen));
                } else {
                        printf("Sorry, try again.\n");
                }
        }

        return 0;
}
