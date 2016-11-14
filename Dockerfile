FROM python:2.7

ADD ./requirements.txt /src/

RUN pip install -r /src/requirements.txt -i https://pypi.douban.com/simple

ADD ./ /src/

WORKDIR /src/
