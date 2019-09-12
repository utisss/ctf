#!/bin/bash

sudo docker build -t intoverflow .
sudo docker run -d --rm --name intoverflow -p 9001:9000 intoverflow
sudo docker cp intoverflow:/pwnable .
