from __future__ import absolute_import, unicode_literals

import datetime
import logging
import time

from celery import shared_task


log = logging.getLogger('celery_sample')


@shared_task
def common(x, y):
    log.info("Handling at：%s", datetime.datetime.now())
    return x + y


@shared_task
def raise_exception():
    raise Exception("Some exception.")


@shared_task
def sleep():
    time.sleep(10)
    return "sleep over."
