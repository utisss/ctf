#!/usr/bin/python2.7
import sys

def main():
    print('Welcome to the ISSS ultra-secure hash table!')

    # set up the galactic hash storage
    storage_size = 2**48
    storage = dict()
    def galactic_hash(s):
        return hash(s) % storage_size

    # ask where the flag should go
    print 'What should be the super secret string be?',
    sys.stdout.flush()
    secret_str = raw_input()
    secret_index = galactic_hash(secret_str)
    storage[secret_index] = open('/home/storage/flag.txt').readlines()

    # take requests to access storage
    print 'What is your personal storage string?',
    sys.stdout.flush()
    user_str = raw_input()
    if not user_str:
        return
    if user_str == secret_str:
        print('Hey reading the flag is not allowed! Use a different string, please.')
        return
    index = galactic_hash(user_str)
    result = '<empty>' if not index in storage else storage[index]
    print('Here\'s what was in your storage: "{}"'.format(result))

if __name__ == '__main__':
    main()
