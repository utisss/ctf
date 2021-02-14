from Crypto.Util.number import bytes_to_long

flag = b'utflag{l0w_eff0rt_Pr0bleM}'

i = bytes_to_long(flag)

a = []
while i > 0:
    a = [i%17]+a
    i //= 17


def get(x):
    if x < 10:
        return str(x)
    return chr(87+x)

print(a)
print(''.join([get(x) for x in a]))
if 'g' in ''.join([get(x) for x in a]):
    print('fuck')
