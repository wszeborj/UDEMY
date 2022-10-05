import requests
import json
from enum import IntEnum
import webbrowser
from pprint import pprint
import urllib.request

Animal_Type = IntEnum('Animal_Type', 'cat dog')
amount_text = 1

cat_websites = {
    'picture': r"https://aws.random.cat/meow",
    'text': r"https://cat-fact.herokuapp.com/facts/random",
}
dog_websites = {
    'picture': r"https://random.dog/",
    'text': r"http://dog-api.kinduff.com/api/facts?number=1"
}


def get_webdata(website: str, **arg):
    r = requests.get(website, **arg)
    try:
        content = r.json()
    except json.decoder.JSONDecodeError:
        print('Niepoprawny format')
        return False
    else:
        return content

def main(websites: dict):
    web_picture = get_webdata(websites['picture'])
    web_text = get_webdata(websites['text'])

# user_choice = int(input('Choose animal: 1-cat, 2-dog\n'))
# user_choice = 1

# if user_choice == Animal_Type.cat:
#     chosen_animal = Animal_Type.cat.name
#     print(f'Your choice is {Animal_Type.cat.name}')
# elif user_choice == Animal_Type.dog:
#     webbrowser.open_new_tab('https://random.dog/')
#     chosen_animal = Animal_Type.dog.name
#     print(f'Your choice is {Animal_Type.dog.name}')


if __name__ == '__main__':
    main(cat_websites)


