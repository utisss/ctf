FROM python:3.8.1-slim-buster

ENV DATABASE_URL postgresql://utctf_prob1:thisisthenonrootpasswordforutctf1@db:5432/utctf_db
ENV FLASK_APP=project/__init__.py

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY /requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
