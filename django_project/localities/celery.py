# coding=utf-8
"""Docstring for this file."""
from __future__ import absolute_import

__author__ = 'ismailsunni'
__project_name = 'healthsites'
__filename = 'celery'
__date__ = '8/27/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from celery import Celery
from django.conf import settings

app = Celery('localities')

CELERY_TIMEZONE = settings.TIME_ZONE

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))