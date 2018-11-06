import socket, array
from tcp_helper import *

serverName = '0.0.0.0'
serverPort = 5000 

def sum_digits(num):
    _sum = 0
    while num > 0:
        _sum += num % 10
        num /= 10

    return _sum

def run():

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    #sockname = clientSocket.getsockname()

    count = 0

    while count < 5:
        response, server_addr = clientSocket.recvfrom(2048)
        #print(response)
        #print(response.decode())
        res = unpackPkt(response, '!L')

        num = res[0]
        count = res[1]
        print(num, count)

        _sum = sum_digits(num)
        datagram = array.array('L')
        datagram.append(_sum)
        datagram.append(count)
        #print(datagram)
        request = packPkt(datagram, '!L')
        clientSocket.sendall(request)
        
    flag, server_addr = clientSocket.recvfrom(2048)
    print("flag: {}".format(flag))

    clientSocket.close()

if __name__ == "__main__":
    run()
