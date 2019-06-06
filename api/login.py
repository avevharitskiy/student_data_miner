from flask import url_for
from urllib.parse import urlencode


def get_login_uri(application_id: int, application_uri: str, scope='friends') -> str:
    login_params = {
        'client_id': application_id,
        'redirect_uri': '{}{}'.format(application_uri, url_for('login')),
        'display': 'popup',
        'scope': scope,
        'response_type': 'code',
    }

    return "https://oauth.vk.com/authorize?{}".format(urlencode(login_params))