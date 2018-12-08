import hashlib
import logging
from flickrpub import exif, db

logger = logging.getLogger('flickrpub.image')


class Image(object):
    def __init__(self, database: db.Database, file_path: str, root_path: str):
        self.database = database
        self.file_path = file_path
        self.root_path = root_path
        self._md5sum = None

    @property
    def md5sum(self, blocksize=65536):
        if self._md5sum:
            return self._md5sum

        h = hashlib.md5()
        with open(self.file_path, "rb") as f:
            for block in iter(lambda: f.read(blocksize), b""):
                h.update(block)
        self._md5sum = h.hexdigest()
        return self._md5sum

    def record(self):
        """ Record the image in the database """
        exif_reader = exif.ExifReader(self.file_path)

        with self.database as db:
            db.add_file(self.file_path, )

    def upload(self):
        """ Upload this Image to Flickr """
