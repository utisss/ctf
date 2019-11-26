#!/bin/bash

sudo docker build -t libc .
sudo docker run -d --rm --name libc -p 9005:9000 libc
sudo docker cp libc:/pwnable .
sudo docker cp libc:/lib/x86_64-linux-gnu/libc-2.23.so .
