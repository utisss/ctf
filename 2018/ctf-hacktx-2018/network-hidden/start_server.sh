# Create our networking vlan
sudo docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=ens160 \
isss-vnet

sudo docker kill apache
sudo docker rm apache
docker run -d --network isss-vnet --ip 192.168.1.8 --name apache -v "$PWD":/var/www/html php:7.2-apache /bin/sleep inf
docker exec apache sh -c 'sed -i "s/80/4550/g" /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf; docker-php-entrypoint apache2-foreground'
