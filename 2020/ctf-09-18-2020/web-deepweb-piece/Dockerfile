FROM alpine:latest

RUN apk update && apk add tor python3
RUN python3 -m ensurepip
RUN pip3 install flask

COPY torrc /etc/tor/torrc
COPY pog.py /
COPY start.sh /
RUN chown -R tor /etc/tor
RUN chmod +x /start.sh
RUN chown -R tor /start.sh
USER tor

ENTRYPOINT ["sh","/start.sh"]

