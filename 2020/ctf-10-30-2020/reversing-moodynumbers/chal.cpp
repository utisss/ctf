#include <iostream>
#include <string.h>
using namespace std;

uint8_t getByte(uint64_t x, uint8_t n) {
    return (x >> 8 * (n % 8)) & 0xFF;
}

uint64_t getKey() {
    /*
    0:  66 0f 76 c0             pcmpeqd xmm0,xmm0
    4:  66 0f 3a df c0 01       aeskeygenassist xmm0,xmm0,0x1
    a:  66 0f 3a df c0 02       aeskeygenassist xmm0,xmm0,0x2
    10: 66 0f 3a df c0 03       aeskeygenassist xmm0,xmm0,0x3
    16: 66 0f 3a df c8 04       aeskeygenassist xmm1,xmm0,0x4
    1c: 66 48 0f 7e c8          movq   rax,xmm1
     */

    asm(".byte 0x66, 0x0F, 0x76, 0xC0, 0x66, 0x0F, 0x3A, 0xDF, 0xC0, 0x01, 0x66, 0x0F, 0x3A, 0xDF, 0xC0, 0x02, 0x66, 0x0F, 0x3A, 0xDF, 0xC0, 0x03, 0x66, 0x0F, 0x3A, 0xDF, 0xC8, 0x04, 0x66, 0x48, 0x0F, 0x7E, 0xC8");

    register long long rax __asm__ ("rax");
    __asm__ ("" :"=r"(rax));
    return rax;
}

void checkInput(string input) {
    uint8_t enc[] = {0x80, 0x6b, 0xfd, 0xc, 0x7a, 0xfc, 0x1b, 0x90, 0xc7, 0x2f, 0xa2, 0x54, 0x7d, 0xf9, 0x54, 0xc3,
                     0xc2, 0x2a, 0xaa, 0x59, 0x23, 0xfe, 0x2, 0xcc, 0x91, 0x2b, 0xa3, 0x6, 0x22, 0xab, 0x6, 0x97, 0xc2,
                     0x2c, 0xff, 0x54, 0x28, 0xfa, 0x55, 0xcc, 0xc3, 0x7d, 0xa8, 0x4, 0x7e, 0xac, 0x58, 0x88,
    };
    int size = input.size();
    if (size != 48) {
        cout << "incorrect";
        exit(1);
    }

    uint8_t data[input.size()];
    register uint64_t key = getKey();
    for (int i = 0; i < size; i++) {
        data[i] = ~(input.at(i) ^ (char) getByte(key, i % 8));
    }
    if (memcmp(enc, data, 48) == 0) {
        cout << "correct";
    }
    else{
        cout<< "incorrect";
    }
}


int main() {
    //utflag{e2094fb4675198eb9d48f90fb73d43a596b3de78}"
    string input;
    cout<<"whats the flag"<<endl;
    cin>>input;
    checkInput(input);
    return 0;
}
