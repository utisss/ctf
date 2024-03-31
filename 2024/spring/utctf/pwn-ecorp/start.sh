#!/bin/bash

sudo qemu-system-mips -m 256 -M malta -kernel /home/user/firmadyne/binaries/vmlinux.mipseb \
    -drive if=ide,format=raw,file=/home/user/firmadyne/scratch/1/image.raw -append "root=/dev/sda1 console=ttyS0 nandsim.parts=64,64,64,64,64,64,64,64,64,64 rdinit=/firmadyne/preInit.sh rw debug ignore_loglevel print-fatal-signals=1 user_debug=31 firmadyne.syscall=0" \
    -nographic \
    -netdev socket,id=net1,listen=:2001 -device e1000,netdev=net1 -netdev socket,id=net2,listen=:2002 -device e1000,netdev=net2 -netdev socket,id=net3,listen=:2003 -device e1000,netdev=net3 | tee /home/user/firmadyne/scratch/1/qemu.final.serial.log
