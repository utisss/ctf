#!/bin/bash

echo "utflag{stack_0verfl0ws_are_c00l}" > /home/stackoverflow/flag.txt
chown root:root /home/stackoverflow/flag.txt
chmod 644 /home/stackoverflow/flag.txt

while [ true ]; do
	su -l stackoverflow -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/pwnable',pty,echo=0,raw,iexten=0"
done;
