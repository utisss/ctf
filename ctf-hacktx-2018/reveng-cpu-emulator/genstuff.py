import binascii
password = b'utctf{KOn9r47Ul471On2_n3cKB34rd}'

pad = b'm1uTZohdxUcVwRMCafXy4mAfcCIo4wyw'

res = binascii.hexlify("".join([chr(ord(x) ^ ord(y)) for x,y in zip(password, pad)]))
print len(res)
print res 

#pad = b'94RZT3gNTB1LcXN5yUfS7qbkpNP6tyvYYOfqM7rsaCrAbeslnHP0W0To8gSWwigc'

#expand = []
'''
for ch in password:
    num = ord(ch)
    add = num / 2
    expand.append(add)
    expand.append(add + num % 2)


enc = [ord(pad[idx]) ^ expand[idx] for idx in xrange(len(expand))]

for a in enc:
    print a
#print "Encrypted: " + "".join(enc)

print "Pad: " + "".join([str(ord(pad[idx]) + " ") for idx in xrange(len(pad))])
'''
