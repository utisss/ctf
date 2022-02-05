#!/bin/bash

echo "utflag{me_and_the_b0ys_at_2am_l00king_f0r_beans}" > /home/printf/flag.txt
chown root:root /home/printf/flag.txt
chmod 644 /home/printf/flag.txt

while [ true ]; do
	su -l printf -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/pwnable',pty,echo=0,raw,iexten=0"
done;
