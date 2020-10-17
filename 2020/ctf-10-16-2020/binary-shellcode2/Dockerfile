FROM ubuntu:16.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev

ARG USER
ENV USER $USER

WORKDIR /

COPY ./shellcode /
COPY ./flag.txt /

COPY start.sh /start.sh
RUN chmod 755 /start.sh

RUN useradd -m $USER

EXPOSE 9000

CMD ["/start.sh"]


