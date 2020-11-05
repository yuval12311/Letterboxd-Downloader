import string

import requests


def hq_magnet_link(response: dict):
    torrents: dict = response["torrents"]["en"]
    highest_res = max(torrents, key=lambda s: int(s[:-1]))
    return torrents[highest_res]['url']


def magnet_for_imdb_link(link: string):
    return hq_magnet_link(requests.get(link).json())

response = requests.get("http://popcorn-ru.tk/random/movie")
print(response.json())
print(hq_magnet_link(response.json()))
