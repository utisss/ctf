#include <stdlib.h>
#include <stdio.h>
#include "pcg_variants.h"

void pprint(char *x, int len) {
	unsigned char c;
	for (int i = 0; i < len; i++) {
		c = x[i];
		if (c > ' ' && c <= '~') {
			if (c == '\\')
				puts("\\\\");
			else
				putchar(c);
		} else {
			printf("\\x%02x", c);
		}
#ifndef NDEBUG
		fflush(stdout);
#endif
	}
	putchar('\n');
}

int main() {
	puts("Number of characters, seed, iterations?");
	int count;
	unsigned long long seed, iterations;
	scanf("%d %llu %llu\n", &count, &seed, &iterations);
	char *buf = malloc(count + 1);
	fgets(buf, count + 1, stdin);
	pcg32_random_t x;
	pcg32_srandom_r(&x, seed, 0);
	pcg32_advance_r(&x, iterations);
	for (int i = 0; i < count / 4; i++) {
		uint32_t r = pcg32_random_r(&x);
		printf("xor %d 0x%08x\n", i, r);
		((uint32_t *)buf)[i] ^= r;
	}
	pprint(buf, count);
}
