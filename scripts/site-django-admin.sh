#!/bin/sh

export PYTHONPATH=/home/wise/data/SITE-CHECK/site-check/src/python
export DJANGO_SETTINGS_MODULE=site_check.settings
export INTERACTIVE_PYTHON_LOG=/home/wise/data/SITE-CHECK/site-check/scripts/py.log

django-admin.py $@
