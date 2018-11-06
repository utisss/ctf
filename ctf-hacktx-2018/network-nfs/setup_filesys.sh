# Create the NFS filesystem
cp -r files filesystem/
chmod 777 filesystem/
cd filesystem

sudo useradd asper -u 28190 -r
sudo chown -R asper asper
sudo chmod -R 555 asper

sudo useradd willy -u 18819 -r
sudo chown -R willy willy
sudo chmod -R 555 willy

sudo useradd tesiuwu -u 48192 -r
sudo chown -R tesiuwu tesiuwu
sudo chmod -R 555 tesiuwu
sudo chmod 400 tesiuwu/Pictures/flag.txt
