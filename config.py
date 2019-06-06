import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    VK_APP_ID = os.environ.get('VK_APP_ID') or '7009086'#'1234567'
    SERVICE_URI = os.environ.get('PERSON_ENVIROMENT_URI') or '492068f8.ngrok.io'
