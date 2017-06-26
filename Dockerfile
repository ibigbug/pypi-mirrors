FROM python:2.7

ADD ./requirements.txt /src/

RUN pip install -r /src/requirements.txt

RUN apt-get update && apt-get install cron -y &&\
  rm -rf /var/lib/apt/lists/*

ADD ./crontab /etc/cron.d/cron-me

RUN chmod 0644 /etc/cron.d/cron-me

RUN crontab /etc/cron.d/cron-me

ADD ./ /src/

WORKDIR /src/

ADD ./scripts/entrypoint /

RUN uwsgi --build-plugin https://github.com/unbit/uwsgi-influxdb

ENTRYPOINT ["/entrypoint"]
