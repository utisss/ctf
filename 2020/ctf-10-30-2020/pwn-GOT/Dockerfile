FROM ubuntu:16.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev

ARG FLAG
ARG USER
ENV USER $USER
ENV FLAG $FLAG

WORKDIR /build
COPY src/. ./src/.
COPY Makefile .
RUN make

WORKDIR /
RUN rm -rf /build/src

COPY start.sh /start.sh
RUN chmod 755 /start.sh

RUN useradd -m $USER

RUN echo "$FLAG" > /home/$USER/flag.txt
RUN chown root:root /home/$USER/flag.txt
RUN chmod 644 /home/$USER/flag.txt

EXPOSE 9000

CMD ["/start.sh"]
