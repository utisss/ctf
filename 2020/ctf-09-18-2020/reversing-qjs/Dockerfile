FROM ubuntu:18.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat

ARG FLAG
ARG USER
ENV USER $USER
ENV FLAG $FLAG

WORKDIR /
COPY . /

RUN chmod 755 /start.sh

RUN useradd -m $USER

RUN echo "$FLAG" > /home/$USER/flag.txt
RUN chown root:root /home/$USER/flag.txt
RUN chmod 644 /home/$USER/flag.txt
RUN export FLAG=$FLAG

EXPOSE 9000

CMD ["/start.sh"]
