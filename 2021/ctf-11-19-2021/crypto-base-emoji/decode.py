import sys
if len(sys.argv) < 2:
    print('No ciphertext supplied!')
    sys.exit(1)

ct = sys.argv[1]
ascii_base = 0x20
ascii_end =  0x7F
emoji_base = 0x1F300
pt = ''
for c in ct:
    codepoint = ord(c) - emoji_base + ascii_base
    pt += chr(codepoint)
print(pt)
