import ConfigParser
import os


def init():
    get_config()

    global url
    url = config.get('GlobalInformation', 'url')

    global userName
    userName = config.get('GlobalInformation', 'userName')

    global password
    password = config.get('GlobalInformation', 'password')
   
def get_config():
    global config
    config = ConfigParser.RawConfigParser()
    package_directory = os.path.dirname(os.path.abspath(__file__))
    config.read(os.path.join(package_directory, 'config.txt'))
