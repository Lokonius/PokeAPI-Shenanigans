from src import api
import re


def main():

    data = api.call("generation", "1")
    max_weight = 0
    fat_pokemon = ""
    count = 0


    for x in data["1"]["pokemon_species"]:

        species_args = re.search("v2/(?P<endpoint>(.*))/(?P<resource>(.*))/", x["url"])
        pokemon_species = api.call(species_args.group("endpoint"), species_args.group("resource"))[species_args.group("resource")]
        pokemon_url = pokemon_species["varieties"][0]["pokemon"]["url"]
        pokemon_args = re.search("v2/(?P<endpoint>(.*))/(?P<resource>(.*))/", pokemon_url)
        pokemon = api.call(pokemon_args.group("endpoint"), pokemon_args.group("resource"))[pokemon_args.group("resource")]

        print(f"{count}/151")
        count += 1

        if pokemon["weight"] > max_weight:

            max_weight = pokemon["weight"]
            fat_pokemon = pokemon["name"]

    print(f"{fat_pokemon} is the fattest pokemon with {max_weight}kg")

if __name__ == "__main__":
    main()