import sys
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from daily import run as run_daily
from pypi_mirrors import run as run_sync

logging.getLogger('apscheduler.executors.default').addHandler(
    logging.StreamHandler(stream=sys.stdout))
logging.getLogger('apscheduler.scheduler').addHandler(
    logging.StreamHandler(stream=sys.stdout))


def start():
    print('cront started')
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_daily, 'interval', days=1)
    scheduler.add_job(run_sync, 'interval', minutes=5,
                      max_instances=1, next_run_time=datetime.now())
    scheduler.start()
