import sqlite3
#from sqlite3 import *

import site_check.settings as settings

def db_file_exists():
    """
    simple boolean to check that the db file is avail.
    """
    db_file = settings.DB_FILE
    try:
        open(db_file, 'r')
        return True
    except IOError:
        return False

def create_sqlite_db():
    """
    """
    conn = sqlite3.connect(settings.DB_FILE)
    c = conn.cursor()

    # Create table
    c.execute('''
create table stocks
                    (date text,
                     trans text,
                     symbol text,
                     qty real,
                     price real)
     ''')

    # Insert a row of data
    c.execute("""insert into stocks
                   values ('2006-01-05','BUY','RHAT',100,35.14)""")

    # Save (commit) the changes
    conn.commit()

    # We can also close the cursor if we are done with it
    c.close()

