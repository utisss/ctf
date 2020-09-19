#!/bin/bash

tor -f /etc/tor/torrc &

sleep 2
cat /tmp/tor/hostname

python3 pog.py
