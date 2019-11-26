#!/bin/bash

echo "utflag{d3l3t_%n_pl5}" > /home/printf/stuffing.txt
chown root:root /home/printf/stuffing.txt
chmod 644 /home/printf/stuffing.txt

while [ true ]; do
	su -l printf -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/pwnable',pty,echo=0,raw,iexten=0"
done;
