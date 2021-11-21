#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include "nessie.h"

char *flag = "\xA4\xDD\x91\x49\x89\x44\x63\x43\xFF\xB8\x85\xA0\x5B\x43\x3E\x85\xD7\xA6\x83\x41\x5B\x1D\xB9\xF5\x93\x94\xFD\xA5\xC9\x6F\x21\xE0\xDF\xF2\x62\xBA\xD6\xF2\x1D\x42\x1E";
char *flagarg;

void iamfork(void);

int main(int argc, char **argv) {
	if (argc != 2 || strlen(argv[1]) > DIGESTBYTES) {
		puts("Please enter the flag.");
		exit(1);
	}
	flagarg = argv[1];
	for (int i = 0; i < 512 * 3 / 2; i++) {
		if (fork() == 0)
			iamfork();
	}
}

void iamfork(void) {
	NESSIEstruct hs;
	NESSIEinit(&hs);
	int val = (getpid() & 511) ^ 0b000101010;
	char buf[DIGESTBYTES];
	NESSIEadd((unsigned char*) &val, sizeof(val) * 8, &hs);
	NESSIEfinalize(&hs, (unsigned char*) &buf);
	for (int i = 0; i < strlen(flag); i++) {
		buf[i] ^= flag[i];
	}
	buf[strlen(flag)] = 0;
	if (!strcmp(flagarg, buf)) {
		printf("Congrats! You got the flag.\n");
	}
	exit(0);
}
