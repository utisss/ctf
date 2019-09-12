#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int user_id;

char *otp = "5F45246490B1F70265F07D415CD57925F19BB84322C982AEAB512884B318A36D6450760E5EF8162DB2351DA54E74259F11601D2FCCC6468F67B771F88F691524";

struct info {
    char encrypt[40];
    void (*print_encryption)(void);
    char choice;
};

void print_otp(void) {
    printf("Enter the string that you want to encrypt with a one time pad.\n");
}

void print_xor(void) {
    printf("Enter the string that you want to encrypt.\n");
}

void otp_encrypt(char *encrypt) {
    size_t len = strlen(encrypt);
    for(int i = 0; i < len; ++i) {
        encrypt[i] ^= otp[i];
    }
}

void xor_encrypt(struct info *information) {
    char xor = (char)user_id;
    size_t len = strlen(information->encrypt);
    for(int i = 0; i < len; ++i) {
        information->encrypt[i] ^= xor;
    }
}
void encrypt(struct info *information) {
    char shouldExit = 0;
    while(1) {
        char choice = information->choice;
        printf("Enter the string you want to encrypt\n"); 
        fgets(information->encrypt, 48, stdin);    
        if(choice == 'a') {
            otp_encrypt(information->encrypt);
        } else {
            xor_encrypt(information);
        }
        printf("Here is your encrypted string: %s\n", information->encrypt);
        printf("Do you want to exit?: y/n\n");
        scanf("%c%*c", &shouldExit);
        free(information);
        if(shouldExit== 'y') {
            printf("Are you sure?\n");
            scanf("%c%*c", &shouldExit);
            
            if(shouldExit != 'n') {
                exit(1); 
            }
        } else if(shouldExit == 'n') {
            information = malloc(sizeof(struct info));
            information->choice = choice;
        } else {
            printf("Someone can't follow instructions\n");
            exit(1);
        }
    }
}

int main(int argc, char **argv) {
    printf("What is your user id?\n");
    scanf("%d%*c", &user_id);
    
    struct info *information = malloc(sizeof(struct info));

    printf("Choose an encryption option:\n");
    printf("a: OTP\n");
    printf("b: Basic XOR\n");
    scanf("%c%*c", &information->choice);
    if(information->choice == 'a') {
        information->print_encryption = &print_otp;
    } else if (information->choice == 'b') {
        information->print_encryption = &print_xor;
    } else {
        printf("Someone can't follow instructions\n");
        return 1;
    }
    encrypt(information);

    
    return 0;
}
