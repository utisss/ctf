# Reverse Engineering: Secret Seed
This problem gives you some information about a Minecraft world, and 
asks you to reverse engineer the seed. Because of the way that Minecraft 
seeds are used, 15 slime chunks can be used to reverse engineer the lower 
48 bits of a seed using some math. Then, the locations of biomes can be 
used to brute force the remaining possibilities to discover the full seed. 
For example, [this project](https://github.com/pisto/minecrack) will do 
this reverse engineering for you. Since the second step is brute-forcing, 
it takes a bit longer (12 minutes on my computer).

## Prompt
My friend set up a Minecraft server with her favorite seed, but 
she won't tell me what it is. I've been secretly collecting some 
data on the server to recover the seed- can you help me find the seed?

**include files here**

_by mattyp_

## Hint
She's running Minecraft version 1.14.

## Flag
`utflag{1453079729188098211}`
