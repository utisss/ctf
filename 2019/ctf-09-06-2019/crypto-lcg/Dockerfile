FROM python:3.8.0b4-alpine3.10
RUN apk add --no-cache socat
COPY src /

WORKDIR /

COPY start.sh /start.sh
RUN chmod 755 /start.sh

RUN adduser -S ret

EXPOSE 9000
USER ret
CMD ["/start.sh"]
