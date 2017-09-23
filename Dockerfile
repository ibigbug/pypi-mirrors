FROM python:2.7

WORKDIR /src/

ADD ./requirements.txt .

RUN pip install -r /src/requirements.txt

ADD . .

ENTRYPOINT ["/usr/local/bin/uwsgi"]
