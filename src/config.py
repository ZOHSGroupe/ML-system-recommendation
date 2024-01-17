from os import environ,path
BASE_DIR = path.abspath(path.dirname(__file__))

class Config(object):
    """set Flask configuration variables from .env file."""
    #general
    DEBUG = environ.get('DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')