# Reverse Engineering: Java
In this challenge, you're given a .class file, which contains Java bytecode. It 
happens that bytecode is higher level than machine code and is thus easier to 
decompile than, say, C++; personally I open the .class file in IntelliJ, which 
decompiles the program automatically.

We can then view the source code, determine that the flag is encrypted using a 
shift cipher; we can then reverse the cipher for each character and get the 
flag. 