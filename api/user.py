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


def get_friends(vkapi: vk.API, user_id: str = None, order: str = None, fields: list = ['domain']):
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

    return filter(lambda user: user.get('can_access_closed', False), result.get('items', [])) if result else []


def get_mutuals(vkapi: vk.API, source_user: int, target_users: list = [],):
    kwargs = {
        'source_uid': source_user,
        'target_uids': target_users,
        'v': server.config.get('API_VERSION')
    }
    result = vkapi.friends.getMutual(**kwargs)
    return result

