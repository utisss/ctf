CC=gcc

all:
	gcc -nostdlib -masm=intel -no-pie -fno-stack-protector -o ${USER} src/pwnable.S

.PHONY: clean
clean:
	-rm *.o
