import sys
if len(sys.argv) < 2:
    print('No plaintext supplied!')
    sys.exit(1)

pt = sys.argv[1]
ascii_base = 0x20
ascii_end =  0x7F
emoji_base = 0x1F300
ct = ''
for c in pt:
    if ord(c) >= ascii_end:
        print('Character "{}" cannot be encoded!'.format(c))
        sys.exit(1)
    codepoint = emoji_base + ord(c) - ascii_base
    emoji = chr(codepoint)
    ct += emoji
print(ct)
