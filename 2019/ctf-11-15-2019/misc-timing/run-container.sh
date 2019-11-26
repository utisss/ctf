#!/bin/bash

sudo docker build -t timing .
sudo docker run -d --rm --name timing -p 9005:9000 timing
