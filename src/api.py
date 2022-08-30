import requests as re
import cache


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


