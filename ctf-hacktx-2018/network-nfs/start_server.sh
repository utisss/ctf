# Start the NFS server
sudo modprobe nfs
sudo modprobe nfsd

# Create our networking vlan
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=ens160 \
isss-vnet

docker run -d --privileged --restart=always \
	-v $(pwd)/filesystem:/nfs \
--network isss-vnet \
-e NFS_EXPORT_DIR_1=/nfs \
-e NFS_EXPORT_DOMAIN_1=\* \
-e NFS_EXPORT_OPTIONS_1=ro,insecure,no_subtree_check,fsid=1 \
--ip 192.168.1.12 \
-p 111:111 -p 111:111/udp \
-p 2049:2049 -p 2049:2049/udp \
-p 32765:32765 -p 32765:32765/udp \
-p 32766:32766 -p 32766:32766/udp \
-p 32767:32767 -p 32767:32767/udp \
fuzzle/docker-nfs-server:latest
