#!/bin/bash

sudo docker build -t zkip .
sudo docker run -d --rm --name zkip -p 9004:9000 zkip
