# Disks of Doom
* **Event:** Spooky CTF
* **Problem Type:** Forensics
* **Difficulty:** Hard
* **Tools Used:** testdisk, losetup, cryptsetup, file, fdisk, find

## Solution
Running `file` on the images reveals some information about them.<br>
`home.img` is an image of a filesystem.<br>
`flashdrive.img` is an image of a boot sector, and it contains a partition table. Given the size, this means that it's probably an image of an entire disk.<br>
<br>
`fdisk -lu flashdrive.img` will display partition table information. There seems to be a partition starting at sector 2048. The sector size is 512 bytes. That means the sector starts at 1048576 bytes. `losetup -o 1048576 /dev/loop0 flashdrive.img` will allow us to set up this disk as a loop device starting from that offset. Trying to mount the filesystem gives an error. The filesystem type is unknown. It's named `crypto_LUKS`. This means the partition is probably using LUKS for encryption. We can use `cryptsetup` to get more information. `cryptsetup luksDump /dev/loop0` prints information about the keyslots. The keyslots are needed for getting the master key to decrypt the partition. There are no keyslots. The LUKS header has been erased. This is as far as we can go with the flashdrive image for now.<br>
<br>
Next, mount `home.img`. It's an ext4 filesystem. Some looking around needs to be done. There are two files in the `gumdrop` directory. One of them is a Python script. It generates a random passphrase based off of the `diceware.txt` file. The RNG is seeded by the time the script was run. If we run `stat password_gen.py` we can see the time the file was last accessed. This may be the time that the file was run to generate the passphrase. Take this time, convert it to a Unix timestamp (make sure to be mindful of the timezone), and use it as the seed for the Python RNG. The passphrase we get is still of no use until we find a backup of the LUKS header file. By looking at the 
`.bash_history` file we can see some of the commands that were used. `sudo cryptsetup luksHeaderBackup --header-backup-file flag.luks /dev/vdb1` is one of those commands. If we run `find . -name flag.luks` in the gumdrop directory, we can see that there is a file in the trash. There is a file called `flag.txt`, but this is not the flag. We can pull out the LUKS header backup and restore it to the flashdrive filesystem with `cryptsetup luksHeaderRestore --header-backup-file flag.luks /dev/loop0`. Now we can unlock the file system with `cryptsetup open /dev/loop0 flag`, and use the password that we found earlier.<br>
<br>
Almost there. Now we just have to mount the file system. The block device is called `/dev/mapper/flag` because of how we called `cryptsetup open`. And there's nothing in there. Or so it seems. Use `testdisk` to look for deleted files, and you'll find the flag in a file called `flag.txt`.
