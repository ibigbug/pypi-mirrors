from apscheduler.schedulers.gevent import GeventScheduler

from .daily import run as run_daily
from .pypi_mirrors import run as run_sync


def start():
    print('cront started')
    scheduler = GeventScheduler()
    scheduler.add_job(run_daily, 'interval', days=1)
    scheduler.add_job(run_sync, 'interval', minutes=5)
