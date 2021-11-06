all: sol

clean:
	rm -f *.o solution

sol.o: sol.c pcg-c-0.94/include/pcg_variants.h

sol: sol.o pcg-c-0.94/src/libpcg_random.a
