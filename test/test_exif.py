import os
from flickrpub.exif import ExifReader


TEST_DIR = os.path.dirname(os.path.realpath(__file__))
DOGE_PATH = '{}/fixtures/image_root/Alex/doge.jpg'.format(TEST_DIR)
EXIF_IMG_PATH = '{}/fixtures/image_root/Alex/exif_img.JPG'.format(TEST_DIR)


class TestExifReader(object):
    def test_init(self):
        o = ExifReader(DOGE_PATH)
        assert isinstance(o, ExifReader)

    def test_load(self):
        o = ExifReader(EXIF_IMG_PATH)
        assert isinstance(o.zeroth_data, dict)
        assert isinstance(o.exif_data, dict)

    def test_property_original_datetime(self):
        o = ExifReader(EXIF_IMG_PATH)
        assert o.original_datetime == b'2018:11:02 11:56:26'
