import shelve
import logging


CACHE_PATH = "cache/cache"
logging.basicConfig(filename="logs/cache.log", encoding="utf-8", level=logging.INFO)


def save_resource(key: str, data: dict):

    with shelve.open(CACHE_PATH) as cache:

        logging.info(f"{key} saved!")

        cache[key] = data
        cache.close()


def load_resource(data: str):

    with shelve.open(CACHE_PATH) as cache:

        if data not in cache.keys():
            raise KeyError("data not yet cached")

        logging.info(f"loaded {data}!")

        resource = cache[data]
        cache.close()
        return resource


def clear():

    with shelve.open(CACHE_PATH) as cache:

        cache.clear()

        logging.info("Cache cleared!")
