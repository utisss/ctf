#!/bin/bash

echo "utflag{ret2_libc_easy}" > /home/libc/flag.txt
chown root:root /home/libc/flag.txt
chmod 644 /home/libc/flag.txt

while [ true ]; do
	su -l libc -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/pwnable',pty,echo=0,raw,iexten=0"
done;
