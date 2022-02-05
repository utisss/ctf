# Coffee Beans
* **Event:** LegumesCTF (ISSS CTF 02-04-2022)
* **Problem Type:** Reversing

## Background
Decompilation is the process of taking a compiled binary and returning it to a 
human-readable, high-level language. 

Java is a programming language that compiles down to bytecode, a machine 
language for the abstract Java Virtual Machine (JVM). The outputted bytecode 
closely reflects the structure of the input program, making decompilation easy.

## Exploit
I simply uploaded the class file to http://www.javadecompilers.com and inspected
the resulting Java code, which seemed fairly easy to understand. 