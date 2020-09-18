#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(char * argv) {
    char * key = "heh, strings won't work here";
    char encrypted[]= {0x1d,0x11,0xe,0x40,0x41,0x14,0xf,0x19,0x5a,0x5d,0x17,0x2c,0x59,0x18,0x3a,0x1c,0x78,0x19,0x45,0x1a,0x0,0x0,0x12,0x7f,0x1c,0x55,0x2d,0x1c,0x7,0x10,0x1a,0x5f,0x45,0x1f,0x32,0xf};
    char buf[256];
    char decrypted[sizeof(encrypted)+1];

    puts("enter the flag:");
    fgets(buf,256,stdin);


    int len = sizeof(encrypted);

    if (strlen(buf)!=len+1){
        puts("try again!");
        return 0;
    }

    for (int i=0; i<len; i++)
        decrypted[i] = key[i%strlen(key)] ^ encrypted[i];
    decrypted[len] = '\0';
    if (strncmp(buf,decrypted,strlen(decrypted)) == 0)
        puts("correct!");
    else
        puts("try again!");


    return 0;
}
