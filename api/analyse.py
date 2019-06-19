import os

import pandas
import vk
from graph_tool import Graph
from graph_tool.draw import sfdp_layout
from graph_tool.inference.minimize import minimize_blockmodel_dl

from api import user


def build_model(vkapi: vk.API, user_for_analyse: dict):
    friend_list, friend_links = __prepare_data(vkapi, user_for_analyse)
    graph = Graph(directed=False)
    vmap = graph.add_edge_list(friend_links.values, hashed=True)
    state = minimize_blockmodel_dl(graph)
    layout = sfdp_layout(graph, groups=state.b)
    state.draw(
        pos=layout,
        vertex_text=vmap,
        vertex_font_size=3,
        vertex_size=3,
        vertex_color=[128, 128, 128, 1],
        output_size=(2000, 2000),
        output="graph.svg")

    with open("graph.svg", 'r') as source:
        graph_image = source.read()

    os.remove("graph.svg")
    return graph_image


def __prepare_data(vkapi: vk.API, user_for_analyse: dict):
    user_for_analyse_id = int(user_for_analyse['id'])
    user_friend_list = list(user.get_friends(vkapi, user_for_analyse_id, fields=['sex']))
    user_friend_dict = {user['id']: user for user in user_friend_list}
    user_ids = list(user_friend_dict.keys())
    user_friend_dict.update({user_for_analyse_id: user_for_analyse})
    mutuals = []

    def _get_info(user_id: int):
        user_data = user_friend_dict[user_id]
        return '''{} {}'''.format(user_data['first_name'], user_data['last_name'])

    while user_ids:
        for friend in user.get_mutuals(vkapi, user_for_analyse_id, user_ids[:100]):
            friend_id = friend.get('id')
            friend_links = []
            for target in friend.get('common_friends'):
                if target in user_friend_dict and [target, friend_id] not in mutuals:
                    friend_links.append([friend_id, target])
            friend_links.append([friend_id, user_for_analyse_id])
            mutuals.extend(friend_links)

        user_ids = user_ids[100:]

    friend_links = pandas.DataFrame(mutuals, columns=['source', 'target'])
    friend_links = friend_links.applymap(_get_info)

    return user_friend_list, friend_links
