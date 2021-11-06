#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pcg_basic.h"

// I really hate the way c handles hex constants
// utflag{party_tricks}
// static char flag[] = "\x97\x08""dj\xdb\x89""A$><\xa5+\x1b\x9e\xc3""c\xd3\xcdpf";
static char flag[] = "\xe3\x0bl;\x93\x95#\xf1|T<\x96""D\xc6\xc0\x10I\xbdQ\x20";


int main(int argc, char** argv) {
	if (argc != 2) {
		puts("Guess the flag!");
		return 1;
	}

	pcg32_random_t x;
	pcg32_srandom_r(&x, 12711602421227413084ULL, 0);

	for (unsigned long long i = 0; i < 18336348997336118836ULL; i++) {
		(void) pcg32_random_r(&x);
#ifndef NDEBUG
		if (!(i % 10000000))
			printf("it %llu\n", i);
#endif
	}

	int bound = strlen(flag) / 4;
	for (int i = 0; i < bound; i++) {
		uint32_t r = pcg32_random_r(&x);
#ifndef NDEBUG
		printf("xor %d 0x%08x\n", i, r);
#endif
		((uint32_t *)flag)[i] ^= r;
	}

#ifndef NDEBUG
	puts(flag);
#endif
	if (strcmp(flag, argv[1])) {
		puts("Nope.");
	} else {
		puts("Yep, that's it!");
	}
}
