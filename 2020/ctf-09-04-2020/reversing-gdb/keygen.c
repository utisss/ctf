#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(char * argv) {
    char * key = "heh, strings won't work here";
    char * flag = "utflag{k33p_yoUr_memory_t0_yourselF}";
    char encrypted[256];

    for (int i =0;i<strlen(flag);i++){
    	 printf("0x%x,", flag[i] ^ key[i%strlen(key)]);
    }



    return 0;
}
