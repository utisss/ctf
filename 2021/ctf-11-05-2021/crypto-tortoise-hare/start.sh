#!/bin/bash

while [ true ]; do
	su -l $USER -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr,nodelay EXEC:'python2.7 /storage.py',pty,echo=0,rawer,iexten=0"
done;
