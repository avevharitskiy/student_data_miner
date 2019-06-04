import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    VK_APP_ID = os.environ.get('VK_APPLICATION_ID') or '1234567'
