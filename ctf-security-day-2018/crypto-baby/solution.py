from binascii import hexlify, unhexlify
import re
import sys
 
def strxor(a, b):     # xor two strings of different lengths
 if len(a) > len(b):
   return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
 else:
   return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
 
def main():

  ciphertexts = ["3c542e2d35225b3e163d313d213a574528163e3c365426207f3229294c7075626353"] 

  target = "2c3b334c20353e4908213a3c3147562c44133f3f2b543f3a11322e3f4c7f7f63725c" 
 
  x = strxor(unhexlify(ciphertexts[0]),unhexlify(target))
  print "Ciphertext[0] xor Target\n"
  crib = raw_input("Enter Crib:>")
  print "Crib\n~%s~"%crib
 
# Crib Drag
  for i in range(len(x)):
    z = x[i:]
    print "\n[%d]"%i
    print "%s"%strxor(z,crib)
 
main()
