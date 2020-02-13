# bf
* **Event:** ISSS Valentime CTF (February 7th, 2020)
* **Problem: Type:** Miscellaneous
* **Difficulty:** Easy

## Background
Brainfuck is an esoteric language designed to simulate a Turing machine and 
thus be Turing-complete. It's really hard to write code in Brainfuck. 

#### Solution
We are given access to a Brainfuck interpreter and are told that the flag
is stored on the tape. We are able to write 5 characters worth of Brainfuck
code. The following code works: 
```[.>]```
This translates to:
    Loop until the current character on the tape is \0. 
    Print the current character on the tape. 
    Move right on the tape. 