#!/bin/bash

sudo docker build -t shellcode .
sudo docker run -d --rm --name shellcode -p 9000:9000 shellcode
sudo docker cp shellcode:/pwnable .
