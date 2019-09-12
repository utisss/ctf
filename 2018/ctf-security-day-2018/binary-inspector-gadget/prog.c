#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

char payload[100];
int wall = 0;

void print_flag() {

    printf("reached print_flag\n");

    if (wall == 0xacce55) {
        system(payload);
    }

    printf("good job\n");
}


unsigned addval_210(unsigned x) { return x + 2425411699U; }

unsigned getval_441() { return 3351742792U; }

void setval_269(unsigned *p) { *p = 2428995912U; }

unsigned addval_184(unsigned x) { return x + 2462550344U; }

void setval_400(unsigned *p) { *p = 3277343479U; }

void setval_435(unsigned *p) { *p = 2425378914U; }

void setval_122(unsigned *p) { *p = 2488834337U; }

void setval_442(unsigned *p) { *p = 3347662929U; }

long add_xy(long x, long y) { return x + y; }

unsigned getval_332() { return 3281049225U; }

unsigned addval_437(unsigned x) { return x + 3375945225U; }

unsigned getval_195() { return 3229928137U; }

unsigned addval_232(unsigned x) { return x + 2430634312U; }

unsigned addval_128(unsigned x) { return x + 3373842825U; }

unsigned addval_343(unsigned x) { return x + 2430634313U; }

unsigned addval_199(unsigned x) { return x + 3380920777U; }

unsigned addval_488(unsigned x) { return x + 3534015113U; }

unsigned addval_261(unsigned x) { return x + 3685007753U; }

void setval_234(unsigned *p) { *p = 1355006344U; }

unsigned addval_351(unsigned x) { return x + 3380923033U; }

unsigned getval_321() { return 3527983497U; }

unsigned getval_391() { return 3252717896U; }

unsigned getval_276() { return 3536115337U; }

unsigned getval_283() { return 3380923017U; }

void setval_461(unsigned *p) { *p = 3353381192U; }

void setval_155(unsigned *p) { *p = 3284830675U; }

unsigned addval_149(unsigned x) { return x + 2496301357U; }

unsigned getval_364() { return 3227571849U; }

unsigned getval_316() { return 3674784137U; }

unsigned addval_156(unsigned x) { return x + 3286272328U; }

void setval_482(unsigned *p) { *p = 3267463447U; }

unsigned addval_139(unsigned x) { return x + 3674789545U; }

void setval_342(unsigned *p) { *p = 2497743176U; }

void setval_349(unsigned *p) { *p = 3224950409U; }

unsigned addval_223(unsigned x) { return x + 3251276182U; }

void setval_144(unsigned *p) { *p = 3286280520U; }

unsigned addval_222(unsigned x) { return x + 3676357001U; }

unsigned getval_466() { return 3376990857U; }

void setval_496(unsigned *p) { *p = 3286273352U; }

void setval_107(unsigned *p) { *p = 3531921049U; }

void setval_251(unsigned *p) { *p = 3676362409U; }

int last() { return 1; }

int get5(int y){
    int x = 5;
    return x;
}

int add5(int x) {
    return x + 5;
}


int changewall() {
    printf("Congrats you broke down the wall\n");
    wall = 0xacce55;
    return wall;
}


void catcat(int key) {
    if(key == 0xb100d) {
        strcat(payload, "cat ");
        printf("good progress...\n");
    }
}
void catflag(int key){

    if(key == 0xba11) {
        strcat(payload, "flag");
        printf("another one down...\n");
    }
}

void addtext(int key, int hello){
    if(key == 0x1555 && hello == 0xc1f101) {
        strcat(payload, ".txt");
        printf("last one....\n");
    }
}

void run() {
    char buffer[100];
    read(STDIN_FILENO, buffer, 256);
}

int main(int argc, char** argv) {
    payload[0] = 0;
    run();
}
