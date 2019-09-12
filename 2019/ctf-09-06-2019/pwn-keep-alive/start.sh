#!/bin/bash

echo "utflag{my_sh3ll_wont_d1e}" > /home/keepalive/flag.txt
chown root:root /home/keepalive/flag.txt
chmod 644 /home/keepalive/flag.txt

while [ true ]; do
	su -l keepalive -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/pwnable',pty,echo=0,raw,iexten=0"
done;
