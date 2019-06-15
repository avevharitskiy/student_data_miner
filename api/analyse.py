from api.tools import get_api
from api import user


def prepare_data(access_token: str, user_for_analyse: str):
    vkapi = get_api(access_token)
    user_friend_list = user.get_friends(access_token, user_for_analyse)
    friend_links = [
        {'id': friend, 'friends': set(user.get_friends(access_token, friend)) & set(user_friend_list)}
        for friend in user_friend_list
    ]


    print(1)