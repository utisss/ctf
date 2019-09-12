#!/usr/bin/env python
import socket
from subprocess import Popen, PIPE
import shlex
import random

TCP_IP = '0.0.0.0'
TCP_PORT = 50287
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data and " " not in data: break
        temp = data.split(" ")
        name = 'ctfsubmission' + str(random.randint(0,999))
        submission = open("submissions/"+name, 'w')
        submission.write(temp[1])
        submission.close()
        cmd = 'bash check.sh ' + temp[0] + " "+ name
        process = Popen(shlex.split(cmd), stdout=PIPE)
        output = process.communicate()[0]
        exit_code = process.wait()
        conn.send(output)
    conn.close()
