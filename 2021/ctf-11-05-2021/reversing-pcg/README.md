# pcg

The provided flag checker uses the [pcg](https://pcg-random.org) random number generator to generate the values that it uses to decrypt the flag. The problem is that it goes through a bazillion iterations before getting there.

You can write your own program to decrypt the flag using their [advance function](https://www.pcg-random.org/using-pcg-c.html#pcg32-advance-r-rngptr-delta) that can get to the nth value in O(log n) time. Solution code is provided with this problem.
