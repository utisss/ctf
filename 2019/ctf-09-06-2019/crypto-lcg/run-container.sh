#!/bin/bash

sudo docker build -t lcg .
sudo docker run -d --rm --name lcg -p 9003:9000 lcg
