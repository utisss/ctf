# Secret Game
# Difficulty: Easy
# Category: Reverse Engineering

Using the Ghidra decompiler and some snooping around (like finding out the 
board is 6x7 and that a win condition involves counting up to four pieces),
we can deduce that we are playing a game of Connect Four against a computer
and that we can get the flag once we beat the computer seven times.

The computer is very dumb at making moves and it's very easy to beat the 
computer seven times in a row and get the flag! I find that the most reliable
strategy is to build horizontally, then vertically if that doesn't work. 