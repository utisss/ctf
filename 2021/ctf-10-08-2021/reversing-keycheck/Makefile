CC=gcc

all:
	gcc -static -fvisibility=hidden -fvisibility-inlines-hidden -s -no-pie -fno-stack-protector -o ${USER} src/pwnable.c

.PHONY: clean
clean:
	-rm *.o
