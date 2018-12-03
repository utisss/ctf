#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cpuid.h>
#include <openssl/md5.h>

// Requires that the user input the CPUID,
// plus the bytes "N" and "Q" at the beginning and end;

int main(int argc, char** argv) {

    MD5_CTX c;
    char buf[512];
    size_t len = strlen(argv[1]);
    memcpy(buf, argv[1], len);
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
