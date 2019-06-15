import vk


def get_api(access_token: str):
    return vk.API(vk.Session(access_token=access_token))
