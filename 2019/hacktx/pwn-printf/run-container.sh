#!/bin/bash

sudo docker build -t printf .
sudo docker run -d --rm --name printf -p 9001:9000 printf
sudo docker cp printf:/pwnable .
