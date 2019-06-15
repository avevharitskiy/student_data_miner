from api.tools import get_api
from server import server
import vk


def get_info(access_token: str, user_id: str = None, fields: list = []):
    vkapi = get_api(access_token)
    kwargs = {
        'user_ids': user_id,
        'fields': ','.join(fields) or None,
        'v': server.config.get('API_VERSION')
    }
    result = vkapi.users.get(**kwargs)
    return result[0] if result else None


def get_friends(access_token: str, user_id: str = None, order: str = None, fields: list = []):
    vkapi = get_api(access_token)
    kwargs = {
        'user_id': user_id,
        'order': order,
        'fields': ','.join(fields) or None,
        'v': server.config.get('API_VERSION')
    }
    try:
        result = vkapi.friends.get(**kwargs)
    except vk.exceptions.VkAPIError:
        result = None

    return result.get('items', None) if result else []
