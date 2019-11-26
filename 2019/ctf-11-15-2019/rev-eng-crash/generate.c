#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cpuid.h>
#include <openssl/md5.h>

// Requires that the user input the CPUID,
// plus the bytes "N" and "Q" at the beginning and end;
char pad[] = {138, 89, 211, 98, 76, 190, 153, 180, 222, 130, 37, 152, 212, 24, 185, 124, 143, 145, 254, 63, 245, 31, 145, 237, 81, 155, 84, 47, 144, 123, 5, 199, 202, 208, 223, 90, 154, 93, 236, 140, 88, 74, 138, 223, 123, 251, 34, 99, 77, 239, 94, 158, 56, 64};

int main(int argc, char** argv) {

    MD5_CTX c;
    char buf[512];
    size_t len = strlen(argv[1]);
    memcpy(buf, argv[1], len);
    for(size_t i = 0; i < len; ++i) {
        buf[i] ^= pad[i];
    }
    unsigned char output[MD5_DIGEST_LENGTH + 1];

    output[MD5_DIGEST_LENGTH] = 0;
    MD5_Init(&c);
    MD5_Update(&c, buf, len);
    MD5_Final(output, &c);
    printf("%s\n", output); 
    //attempt to remove buffer
    for(int i = 0; i < len; ++i) {
        buf[i] = 0;
    }
    return 0;
}
