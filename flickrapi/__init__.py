import flickrapi
import configparser


credentials = configparser.ConfigParser()
credentials.read('credentials.ini')

print(credentials.get('flickrapi', 'api_key'))

