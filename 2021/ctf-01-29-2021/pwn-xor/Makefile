CC=gcc

all:
	gcc -O2 -no-pie -fno-stack-protector -D_FORTIFY_SOURCE=0 -o ${USER} src/pwnable.c

.PHONY: clean
clean:
	-rm *.o
