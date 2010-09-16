#!/usr/bin/env python

from site_check.db import db_file_exists, create_sqlite_db

if not db_file_exists():
    print "creatiing db..."
    create_sqlite_db()
else:
    print "db exists..."




