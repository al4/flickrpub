import logging
import flickrpub.db


logger = logging.getLogger('flickrpub')
# logger.setLevel(logging.DEBUG)


class TestDatabase(object):
    def test_init(self):
        db = flickrpub.db.Database(':memory:')
        assert isinstance(db, object)

    def test_schema_version(self):
        with flickrpub.db.Database(':memory:') as db:
            assert db.version() == flickrpub.db.SCHEMA_VERSION

    def test_execute_insert_select_files(self):
        """ Test that we can insert and select from the files table"""
        with flickrpub.db.Database(':memory:') as db:
            db.execute(""" 
                INSERT INTO files (relative_path) VALUES ('test/file')
            """)
            res = db.execute("""
                SELECT relative_path FROM files
            """).fetchone()
        assert 'test/file' == res[0]
