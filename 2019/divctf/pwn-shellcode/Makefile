CC=gcc

all:
	gcc -no-pie -z execstack -fno-stack-protector -o prog.o src/pwnable.c

.PHONY: clean
clean:
	-rm *.o
