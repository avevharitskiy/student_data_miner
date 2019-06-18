import vk
from api import user
from server import server
import pandas


def build_model(vkapi: vk.API, user_for_analyse: str):
    friend_list, friend_matrix = __prepare_data(vkapi, user_for_analyse)
    print(1)


def __prepare_data(vkapi: vk.API, user_for_analyse: str):
    user_friend_list = list(user.get_friends(vkapi, user_for_analyse, fields=['sex']))
    user_ids = list(map(lambda user: user['id'], user_friend_list))
    mutuals = []
    while user_ids:
        for friend in user.get_mutuals(vkapi, user_for_analyse, user_ids[:100]):
            friend_id = friend.get('id')
            friend_links = list(map(lambda target: [friend_id, target], friend.get('common_friends')))
            friend_links.append([friend_id, int(user_for_analyse)])
            mutuals.extend(friend_links)

        user_ids = user_ids[100:]

    friend_links = pandas.DataFrame(mutuals, columns=['source', 'target'])
    friend_matrix = pandas.crosstab(friend_links.source, friend_links.target)
    idx = friend_matrix.columns.union(friend_matrix.index)
    friend_matrix = friend_matrix.reindex(index=idx, columns=idx, fill_value=0)

    return user_friend_list, friend_matrix
