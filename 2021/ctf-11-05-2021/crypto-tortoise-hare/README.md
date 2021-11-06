# Crypto: Tortoise and Hare
This problem gives you a `python2` program, which implements a simple 
hash table. The user gets to choose where the flag is stored in the 
table by inputting a string that gets hashed to an index using the 
built-in `hash()` function. Then, the user gets to read a value from 
the table by giving another string, but which must be different from 
the previous string. This requirement forces you to find another string 
that collides with the original string's hash value.

`python2`'s built-in `hash()` function is deterministic once seeded 
because of its particular implementation. This property can be abused 
using Floyd's "tortoise and hare" cycle-finding algorithm in order to 
find hash collisions. Once a pair is found, you can input them to read 
the flag. `solve.py` provides an example implementation for reference. 
It's worth noting that this is generally a lot more difficult for 
64-bit hash functions, but the hash function used in this problem is 
modulo the table size, which makes the algorithm much faster. It took 
me about 15 seconds to run on my 13" MacBook Pro.

This problem was actually in an earlier CTF, but the table size was so 
small that it could be brute-forced in a reasonable amount of time.

