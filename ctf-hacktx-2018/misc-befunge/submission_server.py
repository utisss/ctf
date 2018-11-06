#!/usr/bin/env python
import socket
from subprocess import Popen, PIPE
import shlex

TCP_IP = '0.0.0.0'
TCP_PORT = 8888
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("Listening on port " + str(TCP_PORT))

while True:
    conn, addr = s.accept()
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        submission = open('submission.txt', 'w')
        submission.write(data)
        submission.close()
        cmd = 'bash check.sh'
        process = Popen(shlex.split(cmd), stdout=PIPE)
        output = process.communicate()[0]
        exit_code = process.wait()
        conn.send(output)
    conn.close()
    print ""
    
