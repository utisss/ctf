Putting the binary into Ghidra, we can see that 4 bytes are read in, and xor'd with the flag.

Since we know the first 4 characters of the flag should be "utfl", we can determine that the 4 bytes are 105, 100, 107, and 46. xor'ing the string in the binary with these bytes yields the flag.
