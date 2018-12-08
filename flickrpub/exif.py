import logging
import piexif

logger = logging.getLogger('flickrpub.exif')


# http://www.exiv2.org/tags.html

class ExifReader(object):
    """ Extracting exif information from files """
    def __init__(self, file):
        self.file = file
        self._data = None

    def _load(self):
        self._data = piexif.load(self.file)

    def _read_exif_property(self, prop):
        if self._data is None:
            self._load()
        return self._data['Exif'][prop]

    @property
    def exif_data(self):
        if self._data is None:
            self._load()
        return self._data['Exif']

    @property
    def zeroth_data(self):
        if self._data is None:
            self._load()
        return self._data['0th']

    @property
    def datetime_original(self):
        return self.exif_data[piexif.ExifIFD.DateTimeOriginal]
