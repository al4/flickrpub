import os
from flickrpub.db import Database
from flickrpub.image import Image

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = '{}/fixtures/image_root'.format(TEST_DIR)
DOGE_PATH = '{}/Alex/doge.jpg'.format(ROOT_PATH)


class TestImage(object):
    def test_image_init(self):
        im = Image(database=Database(), file_path=DOGE_PATH, root_path=ROOT_PATH)
        assert isinstance(im, Image)

    def test_image_md5sum(self):
        db = Database()
        im = Image(database=db, file_path=DOGE_PATH, root_path=ROOT_PATH)
        assert im.md5sum == 'c09076366e990045dace56c6c7917c6e'
