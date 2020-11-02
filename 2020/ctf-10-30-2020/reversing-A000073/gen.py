trib = [0,0,1]

for i in range(3,1000):
    trib.append(trib[i-1] + trib[i-2] + trib[i-3])

x = b"utflag{int3g3r_s3qu3nc3s_l0l}"
r = b''
for i in range(len(x)):
    print("0x%x, " % ((trib[i*10] % 256) ^ x[i]), end='')
