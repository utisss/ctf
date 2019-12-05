#!/bin/bash

sudo docker build -t ret .
sudo docker run -d --rm --name ret -p 9001:9000 ret
sudo docker cp ret:/pwnable .
