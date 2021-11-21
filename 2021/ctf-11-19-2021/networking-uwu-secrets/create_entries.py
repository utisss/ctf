import sys

flag = 'utflag{domain_names_and_secret_game}'
if len(flag) % 4 != 0:
    print('need a flag of length divisible by 4!')
    sys.exit(1)

i = 0
while i < len(flag):
    ip = ''
    for j in range(i, i+4):
        c = ord(flag[j])
        ip += str(c)+'.'
    ip = ip[:-1]
    print(ip+' '+str(i//4)+'.flag.uwu.com')
    i += 4

