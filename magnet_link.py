import string
import requests
from LB_scrapper import imdb_id


def magnet_from_LB_URL(LB_URL: string) -> string:
    return magnet_from_imdb_id(imdb_id(LB_URL))


def hq_magnet_link(response: dict) -> string:
    torrents: dict = response["torrents"]["en"]
    highest_res = max(torrents, key=lambda s: int(s[:-1]))
    return torrents[highest_res]['url']


def magnet_from_imdb_id(imdb_id: string) -> string:
    return hq_magnet_link(requests.get("http://popcorn-ru.tk/movie/"+imdb_id).json())


print(magnet_from_LB_URL("https://boxd.it/2aWi"))
