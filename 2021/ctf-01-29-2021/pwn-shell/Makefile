CC=gcc

all:
	gcc -no-pie -fno-stack-protector -z execstack -o ${USER} src/pwnable.c

.PHONY: clean
clean:
	-rm *.o
