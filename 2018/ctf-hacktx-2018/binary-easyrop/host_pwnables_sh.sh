#!/bin/bash

#Gonna need it.
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root." 
   exit 1
fi

#This is the user chroot will use to jail the challenge.
USER="test_user"

#This is the name of your challenge.
CHALLENGE="test_challenge"

#This will be the binary that xinetd will run (it's also chroot'd).
#The root directory of this file is /home/$USER/.
BINARY="utcrypt.elf"

#This is the flag that will be wrote to a file called flag.
#The root directory of this file is /home/$USER/.
FLAG="utflag{TURING_SCHOLAR_MASTER_RACE}"

#This is the port xinetd will use.
PORT=1337

#This will copy all the dependencies needed for a given executable.
copy_dependencies() {
	SOURCE="$1"
	DESTINATION="$2"	
	DEPENDENCIES="$(ldd "$SOURCE" | awk '{ print $1 }' | grep -v '(' | grep -v 'not a dynamic executable')"
	DEPENDENCIES="$DEPENDENCIES $(ldd "$SOURCE" | awk '{ print $3 }' | grep -v '(' | grep -v 'not a dynamic executable')"

	for LIB in $DEPENDENCIES; do
		if [ -f "$LIB" ]; then
			cp --parent "$LIB" "$DESTINATION";
		fi
	done
}

export -f copy_dependencies

#Check you have chrootuid installed.
if [ ! -f "/usr/bin/chrootuid" ]; then
	apt install -y chrootuid;
fi

#Check you have xinetd installed.
if [ ! -f "/etc/init.d/xinetd" ]; then
	apt install -y xinetd;
fi

#Check the user exists, if not create the user.
if [ -z "$(getent passwd $USER)" ]; then
    useradd --create-home --password "" $USER;
fi

#Check the user directory exists.
if [ ! -d "/home/$USER" ]; then
    echo "[!] The user directory doesn't exists? There must have been a problem when creating the user's home directory.";
    exit 1;
fi

if [ ! -f "/home/$USER/$BINARY" ]; then
	echo -e "[*] $USER has been created. Go to \"/home/$USER\" and add your binary \"$BINARY\" as well as anything else the challenge needs, then re-run this script.";
	exit 0;
fi

#Prevent user from modifying their own home directory.
#You can setup child directories with other permissions if you want
#but be careful as someone could write their own files and do damage.
chown -R root:root "/home/$USER";

#Change to the user / challenge's directory. This is the root chroot directory.
cd "/home/$USER";

#Check for the binary specified.
if [ ! -f "$BINARY" ]; then
	echo -e "[!] Unable to find \"$BINARY\" in /home/$USER/...\n";
	exit 1;
fi

#Copy libs needed for binary.
copy_dependencies "$BINARY" "."

#Setup challenge environment.
mkdir "bin";
cp "/bin/cp" "./bin/";
cp "/bin/sh" "./bin/";
cp "/bin/bash" "./bin/";
cp "/bin/ls" "./bin/";
cp "/bin/cat" "./bin/";
cp "/bin/echo" "./bin/";

#Copy libs needed for /bin binaries.
for BIN in `ls "./bin"`; do
	copy_dependencies "./bin/$BIN" "."
done

chgrp "$USER" "$BINARY";
chmod -w+r+x "$BINARY";

#Write the flag to a file called flag.
#This is optionl (your flag could be inside the binary? Idk.)
if [ ! -f "flag" ]; then
	echo -e "[*] Adding flag file.";
	echo -e "$FLAG" > "flag";
fi

#Make sure the flag can be read by the user.
chgrp "$USER" "flag";
chmod -w+r+x "flag";

#Write the xinetd config.
if [ ! -f "/etc/xinetd.d/$CHALLENGE" ]; then
SERVICE="
service $CHALLENGE \n 
{ \n
\tdisable         = no \n
\ttype            = UNLISTED \n 
\tport            = $PORT \n
\tsocket_type     = stream \n
\tprotocol        = tcp \n
\twait            = no \n
\tuser            = root \n
\tserver          = /usr/bin/chrootuid \n
\tserver_args     = /home/$USER/ $USER ./$BINARY \n    
\tinstances       = 10 \n
} \n";
    echo -e $SERVICE > /etc/xinetd.d/$CHALLENGE;
    
    #Restart xinetd...
    echo "[*] Creating new service...";
    /etc/init.d/xinetd restart;
    echo -e "\n\n"; 
    /etc/init.d/xinetd status;
    echo -e "\n\n";
    netstat -anpt | grep xinetd;
fi

#and we're done!
echo -e "[*] Done!";
