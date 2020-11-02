FROM ubuntu:16.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev

WORKDIR /

COPY ./graveyard /
COPY ./flag.txt /

COPY start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 9000

CMD ["/start.sh"]


