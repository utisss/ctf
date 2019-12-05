#!/bin/bash

sudo docker build -t arg .
sudo docker run -d --rm --name arg -p 9002:9000 arg
sudo docker cp arg:/pwnable .
