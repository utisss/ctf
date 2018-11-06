from __future__ import print_function


flag = "utflag{i_apologize_for_this_problem}"

for char in flag:
    binary = format(ord(char), 'b') 
    print('   ', end=''),
    for b in binary:
        if b == '0':
            print(' ', end=''),
        else:
            print('\t', end='')
    print('\n', end='')
    print('\t\n', end='')
    print('  ', end='')
