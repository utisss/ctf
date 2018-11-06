flag = 'utflag{humans_dont_like_repeating_themselves}'
binary = ''.join(format(ord(i),'b').zfill(8) for i in flag)
print binary
