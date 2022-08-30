import requests as re
import cache
import re as regex

def call(endpoint, *resources):

    data = {}

    for resource in resources:

        resource_key = "/".join([endpoint, resource])

        try:
            data[resource] = cache.load_resource(resource_key)

        except KeyError:

            resource_url = "/".join(["https://pokeapi.co/api/v2", resource_key])
            response = re.get(resource_url)

            if response.status_code == 404:
                raise ValueError("requested resource not found")

            cache.save_resource(resource_key, response.json())
            data[resource] = response.json()

    return data


def compare_types(type1: str, type2: str):

    data = call("type", type1, type2)[type1]["damage_relations"]

    for relation in data:
        for i in data[relation]:
            if i["name"] == type2:
                info = regex.search("(?P<multiplier>(.*))_(.*)_(?P<direction>(.*))", relation)

                if info.group("direction") == "to":
                    print(f"{type1} deals {info.group('multiplier')} damage to {type2}")
                if info.group("direction") == "from":
                    print(f"{type1} receives {info.group('multiplier')} damage from {type2}")





