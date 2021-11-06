FROM httpd:2.4
RUN a2enmod cgid

FROM ubuntu:16.04

EXPOSE 80

RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install python

#load apache cgi module
RUN a2enmod cgi
RUN service apache2 restart

COPY html/ /var/www/html/
COPY apache2.conf /etc/apache2/apache2.conf

RUN chmod -R u+rwx,g+x,o+x /var/www/html

RUN ln -sf /usr/bin/python /usr/local/bin/python

CMD /usr/sbin/apache2ctl -D FOREGROUND
