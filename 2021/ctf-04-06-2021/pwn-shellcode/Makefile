CC=gcc

all:
	gcc -z execstack -fno-stack-protector -o ${USER} src/pwnable.c

.PHONY: clean
clean:
	-rm *.o
