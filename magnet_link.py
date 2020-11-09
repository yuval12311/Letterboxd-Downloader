import string
import requests
from LB_scrapper import imdb_id, NotFoundError


def magnet_from_LB_URL(LB_URL: string) -> string:
    return magnet_from_imdb_id(imdb_id(LB_URL))


def hq_magnet_link(response: dict) -> string:
    if "torrents" not in response or not response["torrents"]: raise NotFoundError
    torrents: dict = response["torrents"]["en"]
    highest_res = max(torrents, key=lambda s: int(s[:-1]))
    return torrents[highest_res]['url']


def magnet_from_imdb_id(imdb_id: string) -> string:
    if not (response := requests.get("http://popcorn-ru.tk/movie/" + imdb_id)).ok: raise NotFoundError
    return hq_magnet_link(response.json())


