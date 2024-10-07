import hashlib

print('Enter first string: ', end='')
x = input().encode()
print('Enter second string: ', end='')
y = input().encode()

if x == y:
    print('Cheater!')
    exit()

hashx = f'{int(hashlib.sha256(x).hexdigest(), 16):0256b}'
hashy = f'{int(hashlib.sha256(y).hexdigest(), 16):0256b}'

failed = False
for i in range(26):
    if hashx[i] != hashy[i]:
        print(f'Oops! You failed at bit {i}.')
        failed = True

if not failed:
    flag = open('/src/flag.txt', 'r').read();
    print(flag)