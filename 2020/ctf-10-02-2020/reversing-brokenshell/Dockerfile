FROM ubuntu:bionic as BUILDER
RUN apt update
RUN apt install build-essential -y
COPY ./main.c /tmp
RUN gcc /tmp/main.c -o /tmp/badshell

FROM ubuntu:bionic
RUN apt update
RUN apt install socat iputils-ping python3 -y
RUN useradd -ms /bin/rbash pwn
RUN echo "utflag{f3016bf4966893c42ae60c379df561bc84f91e47}" > /flag.txt
WORKDIR /
COPY --from=BUILDER /tmp/badshell /
EXPOSE 31337
USER pwn
CMD socat -dd TCP4-LISTEN:31337,fork,reuseaddr EXEC:"/badshell",pty,echo=0,raw
