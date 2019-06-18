from server import server
import vk


def get_info(vkapi: vk.API, user_id: str = None, fields: list = []):
    kwargs = {
        'user_ids': user_id,
        'fields': ','.join(fields) or None,
        'v': server.config.get('API_VERSION')
    }
    result = vkapi.users.get(**kwargs)
    return result[0] if result else None


def get_friends(vkapi: vk.API, user_id: str = None, order: str = None, fields: list = []):
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


def get_mutuals(vkapi: vk.API, source_user: int, target_user: int, fields: list = []):
    kwargs = {
        'source_uid': source_user,
        'target_uid': target_user,
        'fields': ','.join(fields) or None,
        'v': server.config.get('API_VERSION')
    }
    try:
        result = vkapi.friends.getMutual(**kwargs)
    except vk.exceptions.VkAPIError:
        result = []

    return result

