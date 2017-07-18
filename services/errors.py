import os
from raven import Client

sentry = Client(os.environ.get('SENTRY_DSN'))


if __name__ == '__main__':
    try:
        1 / 0
    except:
        sentry.captureException()
