from binascii import hexlify, unhexlify

def strxor(a, b):     # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def main():
  ms1 = "I HATE WINDOWS! LINUX IS THE BEST."
  ms2 = "YOU ARE WRONG. I LOVE PINTOS MORE!"
  key = "utflag{i_survived_pintos_fall2017}"
  #message1 = "Windows is absolute trash! Everyone knows the best operating system is Linux"
  #message2 = "You must be crazy! PintOS is way better. Here is the flag: i_survived_pintos"
  #key = "supersecretkeythatyou'llneverguessijustneedtofillupallmycharactersasdfghjklqwerty"

  cipher1 = hexlify(strxor(ms1, key))
  cipher2 = hexlify(strxor(ms2, key))

  print cipher1 + " " + cipher2

main()
