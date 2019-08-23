import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SERVICE_URL = os.environ.get('PERSON_ENVIROMENT_URL') or 'http://83c017dd.ngrok.io'
    API_VERSION = os.environ.get('VK_API_VERSION') or '5.95'
