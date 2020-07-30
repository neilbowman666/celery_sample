from __future__ import absolute_import, unicode_literals

import datetime
import logging

from celery import shared_task


log = logging.getLogger('celery_sample')


@shared_task
def add(x, y):
    log.info("Handling at：%s", datetime.datetime.now())
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
