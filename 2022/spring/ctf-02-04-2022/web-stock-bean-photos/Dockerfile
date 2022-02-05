FROM ubuntu:20.04

WORKDIR /usr/src/app
COPY app /usr/src/app
RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
