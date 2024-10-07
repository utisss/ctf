# Random Encryption
* **Event:** SpaceCTF (ISSS CTF 10-04-2024)
* **Problem Type:** Cryptography

## Background
[glibc](https://www.gnu.org/software/libc/)

[srand](https://www.ibm.com/docs/en/i/7.5?topic=functions-srand-set-seed-rand-function)

[LCGs](https://en.wikipedia.org/wiki/Linear_congruential_generator#Advantages_and_disadvantages)

## Exploit

This challenge generates some seemingly random bytes, and then xors them with the flag, outputting
the result. It is in fact true that if a random value is xored with anything, then the result is a
random value. However, the output of rand() is not necessarily a random value, or even a
pseudorandom one.

The implementation of the rand() function in C is handled by stdlib.h. Notably, the most common
implementation (glibc) does the following:

```
unsigned long int next = 1;
int rand(void)
{
    int result;

    next *= 1103515245;
    next += 12345;
    result = (unsigned int) (next / 65536) % 2048;

    next *= 1103515245;
    next += 12345;
    result <<= 10;
    result ^= (unsigned int) (next / 65536) % 1024;

    next *= 1103515245;
    next += 12345;
    result <<= 10;
    result ^= (unsigned int) (next / 65536) % 1024;

    return result;
}

void srand(unsigned int seed)
{
    next = seed;
}
```

Notice that if we do not explicitly call srand(), the next variable is always initialized to 1. So, 
we can recover the same sequence of outputs or rand() by also not calling srand(). After we have the
outputs of rand(), we can xor them with each byte in the output.txt to undo the xoring applied in
chall.c, recovering the original flag. A sample solution which does this is provided in sol.c.