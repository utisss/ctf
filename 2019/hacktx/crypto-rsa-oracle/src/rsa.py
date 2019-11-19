# Decryption oracle

import sys
import random
import gmpy2
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes
import codecs

def input_fix(string):
     return codecs.decode(string,"unicode_escape")


def gen_prime():
    base = random.getrandbits(1024)
    off = 0
    while True:
        if gmpy2.is_prime(base + off):
            break
        off += 1
    p = base + off

    return p

class RSA(object):
    def __init__(self):
        pass

    def generate(self, p, q, e=0x10001):
        self.p = p
        self.q = q
        self.N = p * q
        self.e = e
        phi = (p-1) * (q-1)
        self.d = inverse(e, phi)

    def encrypt(self, m):
        return pow(m, self.e, self.N)

    def decrypt(self, c):
        return pow(c, self.d, self.N)
    
    
def main():
    r = RSA()
    p = gen_prime()
    q = gen_prime()
    r.generate(p, q)

    f = open('FLAG.txt', 'rb')
    flag = f.readlines()[0].strip()
    flag_m = bytes_to_long(flag)

    print("Secret flag", r.encrypt(flag_m))

    
    # Can encrypt anything, even bytes!
    def encrypt_msg():
        print('input the message: ')
        m = input_fix(input().encode())
        M = bytes_to_long(m.encode())
        print(r.encrypt(M))
    
    # Can only decrypt numbers :(
    def decrypt_msg():
        print('input the ciphertext (as an integer): ')
        c = input()
        print(c)
        if c.isnumeric():
            dec = r.decrypt(int(c))
            print("yeet")
            if long_to_bytes(dec) == flag:
                print("No thanks.")
                sys.exit(1)
        else:
            print('Not an integer...')
            sys.exit(1)

        print(dec)
    
    menu = {
        '1' : encrypt_msg,
        '2' : decrypt_msg
    }

    cnt = 2
    while cnt > 0:
        ""
        options = '''Welcome to the RSA encryption and decryption tool!
        1. encrypt_msg
        2. decrypt_msg
        '''
        print(options)
        print('Select option: ')
        choice = input()
        if choice not in menu.keys():
            print("Not a valid choice...")
            sys.exit(1)

        menu[choice]()

        cnt -= 1

main()
