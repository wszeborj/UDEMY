import json

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
        }

json_file = r'C:\Users\user\OneDrive\Dokumenty\VisualStudioCode\sample.json'

#zapisywanie do stringa, indent dodaje wciecia
encodedFilm = json.dumps(film, ensure_ascii=False,) # indent=4, sort_keys=True
# print(encodedFilm)

# zapisywanie do pliku
with open(json_file, 'w', encoding='UTF-8') as file:
    json.dump(film, file, ensure_ascii=False, ) #indent=4, sort_keys=True
#wczytanie stringa json
json_string_film = json.loads(encodedFilm)
print(json_string_film)
# print(json.dumps(json_string_film, indent=4, ensure_ascii=False, sort_keys=True))

#wczytanie pliku json
with open(json_file, encoding='UTF-8') as file:
    json_file_film = json.load(file)
print(json_file_film)

import pprint
pprint.pprint(json_file_film)

