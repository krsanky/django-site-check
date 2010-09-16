#!/usr/bin/env python

import site

#for virtualenv:
# the site module has a handy function addsitedir, which not only adds the directory to the
# pythonpath, but also processes any .pth files it finds
###site.addsitedir(os.path.join(root_dir, 'lib/python2.6/site-packages/'))
site.addsitedir('/home/wise/data/SITE-CHECK/pyvirt/lib/python2.6/site-packages')

import sys, os

#get the path based on where the script runs:
d1 = os.path.realpath(__file__).split('/')
d1.pop()
d1.pop()
d1 = '/'.join(d1) + '/src/python'

# Add a custom Python path.
sys.path.insert(0, d1)
import sys, os

os.environ['DJANGO_SETTINGS_MODULE'] = "site_check.settings"
os.environ['INTERACTIVE_PYTHON_LOG'] = '/home/wise/data/SITE-CHECK/site-check/scripts/py.log'

from site_check.util import check_sites

check_sites()

