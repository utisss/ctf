#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/resource.h>
#include "nessie.h"

char *flag = "\x66\x58\x15\x40\x5E\x2D\x93\xEA\x17\x20\x69\xDB\xFD\xF0\xCD\xB0\x8A\xA3\x8B";
char *key = "yourenotmeanttofigureouttthecrypto";

__attribute__ ((noinline)) static void decrypt(char *key, char *data, char *buf) {
	NESSIEstruct s;
	NESSIEinit(&s);
	NESSIEadd((unsigned char *) key, strlen(key), &s);
	NESSIEfinalize(&s, (unsigned char *) buf);
	for (int i = strlen(data) - 1; i >= 0; i--) {
		buf[i] ^= data[i];
	}
	buf[strlen(data)] = 0;
}

int main() {
	struct rlimit stop;
	stop.rlim_cur = 1023;
	stop.rlim_max = 1023;
	pid_t r;
	char buf[DIGESTBYTES];
	for (int i = 0; i < 65535; i++) {
		setrlimit(RLIMIT_NPROC, &stop);
		r = fork();
		if (r == -1) {
			perror("fork");
			return 1;
		}
	}
	decrypt(key, flag, buf);
	printf("The flag is %s\n", buf);
}
