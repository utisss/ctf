# GG-16 Emulator
# Difficulty: Medium

This is a reverse engineering challenge, inspired by the custom bytecode used in ReCaptcha. 

For the reverse engineering route, you need to read through the code in bytecode.js to figure 
out how each instruction works. Then you can reverse engineer the code contained in 
flagCheck.js Information on both of these are included in this repo. The code accepts user 
input, interprets each character as a 16-bit integer, then multiplies it by 13 and adds 17. 
Finally it compares it to the "enc" array in checkFlag(). The decryption is then done by 
interpreting each pair of numbers in "enc" as a 16-bit little-endian integer, then subtracting
17 and dividing by 13. 

You can also note that the code is not constant-time, and modify the JavaScript code to keep
track of how many instructions are being run for each input. From here, a simple timing side-
channel attack will work. 

For example, we can instrument the bottom of the checkFlag() function as such, to keep track
of how many instructions the CPU runs for before it traps. Since the CPU will trap earlier if
the 1st character is wrong vs if the 2nd character is wrong, for instance, this helps us guess
the flag one character at a time.

```
    const cpu = new CPU(mmu);
*   const ccnt = 0;

    while(true) {
        try {
            cpu.evalInstr();
*           ccnt++;
        }catch(e) {
*           console.log(ccnt);
            if(e === "invalid opcode: aa") {
                return true;
            }
            return false;
        }
    }
```