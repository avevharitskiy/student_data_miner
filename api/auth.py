import datetime
import json

import requests
from flask import redirect, request, url_for

from server import server


def get_access_token(code: str) -> str:
    response = requests.get(
        url='https://oauth.vk.com/access_token',
        params={
            'client_id': server.config.get('VK_APP_ID'),
            'client_secret':  server.config.get('VK_APP_SECRET'),
            'redirect_uri': requests.compat.urljoin(server.config.get('SERVICE_URL'), url_for('login')),
            'code': code
        }
    )

    result = json.loads(response.text)

    if 'access_token' in result:
        expires_date = datetime.datetime.now() + datetime.timedelta(seconds=result['expires_in'])

        return result['access_token'], expires_date


def decorator(func):
    def wrapper(*args, **kwargs):
        if 'access_token' in request.cookies:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    wrapper.__name__ = func.__name__
    return wrapper


def login(func):
    def wrapper(*args, **kwargs):
        if 'access_token' not in request.cookies:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user_page'))

    wrapper.__name__ = func.__name__
    return wrapper
