FROM python:rc-alpine3.12

WORKDIR /usr/src/app
RUN apk update && apk add python3-dev

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY app.py /usr/src/app/
COPY static/ /usr/src/app/static/
COPY templates/ /usr/src/app/templates/
RUN adduser --disabled-password --gecos "" --no-create-home worker
RUN mkdir -p /var/app/data
RUN chown worker:nobody /var/app/data
USER worker:nobody
ENV DATA_DIR=/var/app/data

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["-m", "gunicorn", "--chdir", "/usr/src/app", "-b", "0.0.0.0:8000", "-w", "1", "app:app"]
