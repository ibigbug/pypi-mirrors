FROM python:2.7

ADD ./requirements.txt /src/

RUN pip install -r /src/requirements.txt

ADD ./ /src/

WORKDIR /src/
