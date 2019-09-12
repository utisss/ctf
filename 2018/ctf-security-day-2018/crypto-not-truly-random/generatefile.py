import os

def random_1():
    return ord(os.urandom(1)) % 2

length = 4384
def generate_random_bitstring():
    string = ""
    for i in range(0, 4384):
        if random_1() == 1:
            string += '0'
        else:
            string += '1'
    return string

output = open('file.txt', 'w')
for i in range(0, 99998):
    output.write(generate_random_bitstring() + '\n')

output.close()
