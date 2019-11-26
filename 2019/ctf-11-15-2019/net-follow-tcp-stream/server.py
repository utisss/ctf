from socket import *

f = open('flag.txt', 'r')
flag = f.read()

s = socket(AF_INET, SOCK_STREAM)

s.bind(('0.0.0.0', 8080))
s.listen()

while True:
    cli, addr = s.accept()

    for c in flag:
        cli.send(c.encode('ascii'))
    cli.close()
