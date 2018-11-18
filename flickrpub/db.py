import logging
import sqlite3


DB_FILE = 'flickrpub.sqlite'

logger = logging.getLogger('flickrpub.db')


class Database(object):
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

    def execute(self, statement):
        """ Execute the given SQL statement """
        self.conn.execute(statement)
        self.conn.commit()

    def _table_exists(self, table_name):
        res = self.conn.execute(
            """ SELECT name FROM sqlite_master WHERE type='table' AND name='{}' 
            """.format(table_name)
        ).fetchall()
        return True if (table_name, ) in res else False

    def _initialise(self):
        logger.info("Initialising sqlite database '{}'".format(self.sqlite_file))
        self.conn.execute(""" CREATE TABLE files (id INTEGER PRIMARY KEY) """)
        self.conn.execute(""" ALTER TABLE files ADD COLUMN 'file_name' TEXT NOT NULL UNIQUE """)
        self.conn.execute(""" ALTER TABLE files ADD COLUMN 'md5' TEXT """)
        # SQLite has no bool type
        self.conn.execute(""" ALTER TABLE files ADD COLUMN 'uploaded' INTEGER """)
        self.conn.commit()

    def add_file(self, file_name, md5, uploaded=0):
        self.execute("""
            INSERT INTO files(file_name, md5, uploaded) VALUES({fn}, {md5}, {upl})
            """.format(fn=file_name, md5=md5, upl=uploaded))

    def mark_uploaded(self, file_name):
        self.execute("""
            UPDATE files SET uploaded = 1 WHERE file_name = '{}'
        """.format(file_name))
