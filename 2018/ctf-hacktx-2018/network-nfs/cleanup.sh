docker kill $(docker container list | awk 'FNR==2{print $1}')
umount -f -l testdir
rm -rf testdir
rm -rf filesystem
sudo userdel asper
sudo userdel tesiuwu
sudo userdel willy
