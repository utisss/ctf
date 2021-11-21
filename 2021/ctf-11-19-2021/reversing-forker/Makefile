all: genflag forker

genflag: gen_flag.c Whirlpool.c
	$(CC) $(CFLAGS) $^ -o $@

forker: forker.c Whirlpool.c
	$(CC) $(CFLAGS) -O1 $^ -o $@
	strip --strip-unneeded $@

clean:
	rm -f googleable
