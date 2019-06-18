import vk
from api import user
from server import server
import pandas
import graph_tool


def build_model(vkapi: vk.API, user_for_analyse: str):
    data = __prepare_data(vkapi, user_for_analyse)
    print(1)


def __prepare_data(vkapi: vk.API, user_for_analyse: str):
    user_friend_list = user.get_friends(vkapi, user_for_analyse,)
    #user_friend_list.append(user_for_analyse)
    friends_count = len(user_friend_list)
    user_ids = dict(zip(user_friend_list, range(friends_count)))
    friend_links = pandas.

    for friend in user_friend_list:
        mutuals = map(lambda user: user_ids[user], user.get_mutuals(vkapi, user_for_analyse, friend))
        print(1)
    return user_friend_list
