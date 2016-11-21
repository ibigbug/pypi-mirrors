pypi-mirrors
============

Very simple tool that pings the PyPI mirrors and tells us when they were updated last.

I threw this together very quickly as a proof of concept feel free to fork, and send pull requests.

Docker Image
------------

https://hub.docker.com/r/ibigbug/pypi-mirrors/

Config
------

Redis
~~~~~
It requires redis in order to cache some of the data. For local development it is assuming it to be running
at localhost:6379 db:1 and no password. see ``config.py`` for more info.

GeoIP
~~~~~
In order to get the IP address geolocation lookup, you need to sign up for an account from http://ipinfodb.com/register.php . If you don't have the env variable set, you will not have access to the geo location information. set IPLOC_API_KEY with the API key they give you.

Email & Twitter
~~~~~~~~~~~~~~~
Pass the corresponding environment variables to enable email & twitter notifications.


Environment variables
~~~~~~~~~~~~~~~~~~~~~

env variables::

   docker run \
       -e 'CACHE_REDIS_HOST=localhost' \
       -e 'CACHE_REDIS_PORT=6379' \
       -e 'IPLOC_API_KEY=<value>' \
       -e 'TWITTER_CONSUMER_KEY=<value>' \
       -e 'TWITTER_CONSUMER_SECRET=<value>' \
       -e 'TWITTER_ACCESS_KEY=<value>' \
       -e 'TWITTER_ACCESS_SECRET=<value>' \
       -e 'EMAIL_HOST=<value>' \
       -e 'EMAIL_PORT=<value>' \
       -e 'EMAIL_USER=<value>' \
       -e 'EMAIL_PASSWORD=<value>' \
       -e 'EMAIL_FROM=<value>' \
       -e 'EMAIL_TO=<value>' \
       -e 'EMAIL_BCC=<value>' \
       -e 'EMAIL_TO_ADMIN=<value>'\
       -v /tmp/:/tmp/ \
       ibigbug/pypi-mirrors \
       uwsgi  -w wsgi -s /tmp/uwsgi.sock --logto=/var/log/uwsgi/uwsgi.log --chdir=/src/ --chmod-socket=666


How it works
------------
The ``pypi_mirrors.py`` script runs via a cron job and puts data into redis. There is one webpage that pull the data from redis and
displays it. There is a daily cron job that runs and sends out notifications if the mirrors are out of date.

Demo
----
http://www.pypi-mirrors.org

How to help
-----------
Pick one of the things on the TODO list and implement it and send a pull request.

Running locally
---------------
Make sure redis is running

1. Collecting Data::

    $ python pypi_mirrors.py

2. Running web server::

    $ python app.py
    # connect to http://localhost:5000 in browser


TODO:
-----
- [ ] Create a setup.py and add to PyPI
- [ ] Add better documentation
- [x] Make Docker Image
