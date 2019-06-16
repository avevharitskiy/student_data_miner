import vk
from api.tools import get_api
from api import user
from server import server
import graph_tool

def build_model(access_token: str, user_for_analyse: str):
    data = __prepare_data(access_token, user_for_analyse)
    print(1)


def __prepare_data(access_token: str, user_for_analyse: str):
    vkapi = get_api(access_token)
    user_friend_list = user.get_friends(access_token, user_for_analyse, fields=['domain'])

    for friend in user_friend_list:
        try:
            friend['mutual'] = vkapi.friends.getMutual(
                source_id=user_for_analyse,
                target_uid=friend['id'],
                v=server.config.get('API_VERSION')
            )
        except vk.exceptions.VkAPIError:
            friend['mutual'] = []
            continue
    return user_friend_list
