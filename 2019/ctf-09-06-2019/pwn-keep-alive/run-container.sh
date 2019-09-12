#!/bin/bash

sudo docker build -t keepalive .
sudo docker run -d --rm --name keepalive -p 9002:9000 keepalive
