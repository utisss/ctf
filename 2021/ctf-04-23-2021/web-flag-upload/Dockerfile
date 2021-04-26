FROM ubuntu:20.04

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install --upgrade pip
COPY /requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /usr/src/app
COPY flag.txt /flag.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["/usr/src/app/app.py"]
