#!/bin/bash

while [ true ]; do
	socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/graveyard',pty,echo=0,raw,iexten=0
done;

