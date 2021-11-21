all: genflag fowkbowmb

genflag: gen_flag.c Whirlpool.c
	$(CC) $(CFLAGS) $^ -o $@

fowkbowmb: fowkbowmb.c Whirlpool.c
	$(CC) $(CFLAGS) -O1 $^ -o $@
	strip --strip-unneeded $@

clean:
	rm -f genflag fowkbowmb
