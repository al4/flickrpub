import logging
import flickrpub.db


logger = logging.getLogger('flickrpub')
logger.setLevel(logging.DEBUG)


class TestDatabase(object):
    def test_init(self):
        db = flickrpub.db.Database(':memory:')
        assert isinstance(db, object)

    def test_schema_version(self):
        with flickrpub.db.Database(':memory:') as db:
            assert db.version() == flickrpub.db.SCHEMA_VERSION

