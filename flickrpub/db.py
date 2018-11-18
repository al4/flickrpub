import os
import logging
import sqlite3


DB_FILE = 'flickrpub.sqlite'

logger = logging.getLogger('flickrpub')


class Database():
    def __init__(self, sqlite_file=DB_FILE):
        self.sqlite_file = sqlite_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cursor = self.conn.cursor()

        if not self._table_exists('files'):
            self._initialise()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error("{} in database connection: {}\n{}".format(exc_type, exc_val, exc_tb))
        self.conn.close()

    def _table_exists(self, table_name):
        res = self.conn.execute(
            """SELECT name FROM sqlite_master WHERE type='table' AND name='{}'""".format(
                table_name
            )).fetchall()
        return True if (table_name, ) in res else False

    def _initialise(self):
        self.conn.execute(""" CREATE TABLE files (id INTEGER PRIMARY KEY) """)
        self.conn.execute(""" ALTER TABLE files ADD COLUMN 'file_name' TEXT """)
        self.conn.execute(""" ALTER TABLE files ADD COLUMN 'md5' TEXT """)
        self.conn.commit()
