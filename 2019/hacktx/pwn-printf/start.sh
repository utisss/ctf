#!/bin/bash

echo "utflag{n1c3_f0rm4t_str1ng}" > /home/printf/flag.txt
chown root:root /home/printf/flag.txt
chmod 644 /home/printf/flag.txt

while [ true ]; do
	su -l printf -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/pwnable',pty,echo=0,raw,iexten=0"
done;
