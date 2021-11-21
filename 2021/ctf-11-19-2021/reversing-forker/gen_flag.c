#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "nessie.h"

int main(int argc, char** argv) {
	if (argc != 3) exit(1);
	int flagkey = atoi(argv[1]);
	char *flag = argv[2];
	char buf[DIGESTBYTES];
	NESSIEstruct s;
	NESSIEinit(&s);
	NESSIEadd((unsigned char*) &flagkey, sizeof(flagkey) * 8, &s);
	NESSIEfinalize(&s, (unsigned char*) &buf);
	if (strlen(flag) > DIGESTBYTES) exit(2);
	for (int i = strlen(flag) - 1; i >= 0; i--) {
		buf[i] ^= flag[i];
	}
	display((unsigned char*) buf, strlen(flag));
}
