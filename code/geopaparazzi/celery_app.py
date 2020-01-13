from __future__ import absolute_import

import os
import logging

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geopaparazzi.settings')
app = Celery('geopaparazzi')
logger = logging.getLogger(__name__)


def _log(msg, *args):
    logger.info(msg, *args)


app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()