# Create our networking vlan
sudo docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=ens160 \
isss-vnet

# sudo docker pull piesecurity/apache-struts2-cve-2017-5638
sudo docker run -d --name struts2 --network isss-vnet --ip 192.168.1.10 -p 32771:8080 piesecurity/apache-struts2-cve-2017-5638
CONTAINER_ID=$(sudo docker container list | grep struts | awk '{print $1}')

echo "Waiting for container to boot..."
sleep 5

echo "Copying modified config..."
sudo docker cp backup.xml $CONTAINER_ID:/usr/local/tomcat/webapps/ROOT/WEB-INF/classes/struts.xml

echo "Copying flag..."
sudo docker cp flag.txt $CONTAINER_ID:/usr/local/tomcat/flag.txt

echo "Shutting down container..."
sudo docker exec $CONTAINER_ID /usr/local/tomcat/bin/shutdown.sh
sleep 5

echo "Starting container again..."
sudo docker start $CONTAINER_ID
