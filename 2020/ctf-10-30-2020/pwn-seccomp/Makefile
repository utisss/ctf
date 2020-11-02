CC=gcc

all:
	clang -no-pie -fno-stack-protector -o ${USER} -lseccomp src/pwnable.c

.PHONY: clean
clean:
	-rm *.o
