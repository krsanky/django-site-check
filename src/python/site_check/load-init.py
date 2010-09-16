#!/usr/bin/env python

import settings

import sqlite3
#from sqlite3 import *

conn = sqlite3.connect(settings.INIT_DB_FILE)
curs = conn.cursor()


curs.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")

conn.commit()

curs.close()


