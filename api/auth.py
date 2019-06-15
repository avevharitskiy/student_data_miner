import json

import requests
from flask import url_for

from server import server
from api.tools import get_api


def get_access_token(code: str) -> str:
    response = requests.get(
        url='https://oauth.vk.com/access_token',
        params={
            'client_id': server.config.get('VK_APP_ID'),
            'client_secret':  server.config.get('VK_APP_SECRET'),
            'redirect_uri': requests.compat.urljoin(server.config.get('SERVICE_URI'), url_for('login')),
            'code': code
        }
    )

    result = json.loads(response.text)

    if 'access_token' in result:
        return result['access_token']


def validate_access_token(access_token: str):
    vkapi = get_api(access_token)
    try:
        vkapi.users.get(v=server.config.get('API_VERSION'))
    except vk.exceptions.VkAPIError:
        return False

    return True
