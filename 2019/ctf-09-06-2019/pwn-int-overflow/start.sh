#!/bin/bash

echo "utflag{b1zza_tim3}" > /home/intoverflow/flag.txt
chown root:root /home/intoverflow/flag.txt
chmod 644 /home/intoverflow/flag.txt

while [ true ]; do
	su -l intoverflow -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/pwnable',pty,echo=0,raw,iexten=0"
done;
