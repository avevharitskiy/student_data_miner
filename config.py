import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    VK_APP_ID = os.environ.get('VK_APP_ID') or '7009086'#'1234567'
    SERVICE_URI = os.environ.get('PERSON_ENVIROMENT_URI') or 'http://69502196.ngrok.io'
    VK_APP_SECRET = os.environ.get('VK_APP_SECRET') or 'IHd0tMS1DKnx4NMJuDDu'
    API_VERSION = os.environ.get('VK_API_VERSION') or '5.95'
