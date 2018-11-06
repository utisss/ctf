# Solution

This is a simple buffer overflow. You can pass in something like
"A"\*16+"\x02\x00\x00\x00" to get result to overflow correctly and set auth =2
