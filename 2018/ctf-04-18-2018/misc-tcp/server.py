import socket, array, random
from multiprocessing import Process
from tcp_helper import *

FLAG = "utflag{TCP}"

IP = '0.0.0.0'
PORT = 5000

MAX_LONG = 2**32-1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = (IP, PORT)
sock.bind(server_address)
sock.listen(1)
print("Listening on port {}...".format(PORT))

def sum_digits(num):
    _sum = 0
    while num > 0:
        _sum += num % 10
        num /= 10

    return _sum


def rand_nums(conn):

    count = 1

    while count <= 5:
        print(count)
        num = random.randint(0, MAX_LONG)
        print("rand num: {}".format(num))

        actual_sum = sum_digits(num)
        print("actual_sum: {}".format(actual_sum))

        datagram = array.array('L')
        datagram.append(num)
        datagram.append(count)
        print(datagram)

        request = packPkt(datagram, '!L') 
        print(request)
        conn.sendall(request)

        # Get response
        response, client_addr = conn.recvfrom(2048)
        res = unpackPkt(response, '!L')

        resp_sum = res[0]
        resp_count = res[1]

        if actual_sum == resp_sum and count == resp_count:
            count += 1            
        else:
            # Send error
            conn.close()
            exit(0)

    # Send flag
    print("sending flag")
    conn.send(FLAG.encode())

    conn.close()
    exit(0)
    

while True:
    conn, client_addr = sock.accept()
    print("got new connection from {}".format(client_addr))

    p = Process(target = rand_nums, args=(conn,))
    p.start()
