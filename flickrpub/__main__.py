import flickrapi
import configparser
from argparse import ArgumentParser
import logging

logging.basicConfig(format='%(message)s')
logger = logging.getLogger('flickrapi')


if __name__ == "__main__":
    credentials = configparser.ConfigParser()
    credentials.read('credentials.ini')

    parser = ArgumentParser()
    parser.add_argument('--collection', '-c', help='Flickr collection to use')
    parser.add_argument('--watch', '-w', action='store_true',
                        help='Watch the directory rather than upload once')
    parser.add_argument('directory', help='Directory upload from')
    parser.parse_args()

    logger.info(credentials.get('flickrapi', 'api_key'))

    flickr = flickrapi.FlickrAPI(
        api_key=credentials.get('flickrapi', 'api_key'),
        secret=credentials.get('flickrapi', 'secret'),
    )

    print(flickr)
    flickr.authenticate_via_browser(perms='write')

