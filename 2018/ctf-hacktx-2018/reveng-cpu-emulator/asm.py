#printf(str + 0+ #fgets(strings + 270, 30, stdin)
import binascii
import struct

p32 = lambda x : struct.pack("I", x) 
instructions = [0x21, 0, 0, 0x22, 270, 30, 0x67, 0, 0, 0x34, 2, 270, 0x67, 2, 0, 0x34, 2, 270, 0x67, 3, 0, 0x34, 3, 58, 0x55, 0, 32, 0x56, 45, 45, 0x61, 0, 91, 0x56, 39, 39, 0x21, 36, 36, 0x69, 0x69, 0x69, 0x21, 46, 46, 0x69, 0x69, 0x69, 0x5, 1, 2, 0x5, 4, 3, 0x14, 1, 4, 0x98, 0, 1, 0x34, 0, 1, 0x34, 2, 1, 0x34, 3, 1, 0x93, 24, 24]

rom = open("prog.rom", "w+")
#print out memory
for instr in instructions:
    rom.write(p32(instr))

#write out the rest of the memory
for x in xrange(300 - len(instructions)):
    rom.write(p32(0))

#write out the strings
str1 = b"Please enter the correct password:\n\x00"
print len(str1)
str2 = b"Correct!\n\x00"
print len(str1 + str2)
str3 = b"Incorrect!\n\x00"
print len(str1 + str2 + str3)
str4 = b"m1uTZohdxUcVwRMCafXy4mAfcCIo4wyw\x00"
rom.write(str1)
rom.write(str2)
rom.write(str3)
#58 bytes
rom.write(b"m1uTZohdxUcVwRMCafXy4mAfcCIo4wyw\x00")
#91 bytes
result = binascii.unhexlify("184516203c14232b166c1162400721775657171706322f5500080b5c00051d0a")
rom.write(result)
rom.write("\x00")
#124
rom.write("\x00" * 300)

'''
36 bytes
printf("Please enter the correct password:\n\x00"); 0
0x21 0 0

fgets(strings + 270, 32, stdin); 1
0x22 270 32

reg[0] &= 0 2
0x67 0 0

reg[2] &= 0 3
0x67 2 0

reg[2] += 270 4
0x34 2 270

reg[3] &= 0 5
0x67 3 0

reg[3] += 58 6
0x34 3 58

cmp_reg = reg[0] - 32 7
0x55 0 33

jmp to instr 15 if cmp_reg != 0 8
0x56 45 45

strcmp(mem, strings + 91) 9
0x61 0 91

jmp to instr 13 if cmp_reg != 0 10
0x56 39 39

printf("Correct!\n"); 11
0x21 36 36

exit 12
0x69 0x69 0x69

printf("Incorrect!\n"); 13
0x21 46 46

exit 14
0x69 0x69 0x69

START_CHECK:
mov regs[1], strings + regs[2] 15
0x5 1, 2 

mov regs[4], strings + regs[3] 16
0x5 4, 3 

regs[1] ^= regs[4] 17
0x14 1 4

mov mem[regs[0]], regs[1]
0x98 0 1

add regs[0], 1
0x34 0 1

add regs[2], 1
0x34 2 1

add regs[3], 1
0x34 3 1

jmp instr 7
0x93 21 21
'''
