# Forensics - Flash
### @aadhi0319

First, you will need to install Sleuth Kit or Atopsy. Atopsy is easier to use, but Sleuth Kit runs on the command line, so I prefer using it. After unzipping the file, you should get a file named `usb.img`.

`img_stat usb.img`

This command tells you that this file is a raw image for an 8 GB drive. The sector size is 512.

`mmls usb.img`

This command lists partitions in the image. As you can see, there are three partitions in this drive. The partition that says "Win95 FAT32" is interesting because this is the format Windows uses to save files to drives. This command also tells us that this partition is at offset 64.

`fsstat -o 64 usb.img`

This command shows us file system information for the partition in question. 

`fls -o 64 usb.img`

This command lists directories (some may have been deleted). We see an interesting folder called `ctf` at inode 16.

`fls -o 64 usb.img 16`

This command opens the directory discovered in the last step. It lists a file named `flag.txt` with inode 5338502.

`icat -o 64 usb.img 5338502`

This command prints the contents of `flag.txt` to the console. We see that the flag is `utflag{l3arn_4ll_th3_53cr3t$_w!th_for3n5ics}`.
