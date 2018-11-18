import flickrapi
import configparser
from argparse import ArgumentParser
import logging
import os
from flickrpub.db import Database

logging.basicConfig(format='%(levelname)s - %(message)s')
logger = logging.getLogger('flickrpub')
logger.setLevel(logging.INFO)


def main():

    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Print debug log messages')
    parser.add_argument('--collection', '-c', help='Flickr collection to use')
    parser.add_argument('--watch', '-w', action='store_true',
                        help='Watch the directory rather than upload once')
    parser.add_argument('directory', help='Directory upload from')
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    with Database() as cursor:
        res = cursor.execute("SELECT * FROM 'files'")
        logger.debug(res)

    list_files(args.directory)


def flickrapi_auth():
    logger.info("Authenticating to Flickr...")
    credentials = configparser.ConfigParser()
    credentials.read('credentials.ini')

    flickr = flickrapi.FlickrAPI(
        api_key=credentials.get('flickrapi', 'api_key'),
        secret=credentials.get('flickrapi', 'secret'),
    )
    flickr.authenticate_console(perms='write')


def list_files(dir):
    """ List all files in a directory """
    l = os.listdir(dir)
    logger.debug(l)



def upload_photo(private=True):
    """ Upload a photo """



if __name__ == "__main__":
    main()
