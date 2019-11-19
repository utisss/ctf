#!/bin/bash

sudo docker build -t rsa .
sudo docker run -d --rm --name rsa -p 9003:9000 rsa
