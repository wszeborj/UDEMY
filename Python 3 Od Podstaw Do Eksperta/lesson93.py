import requests
import json
from enum import IntEnum
import webbrowser
from pprint import pprint
import urllib.request
from PIL import Image, ImageTk
import tkinter as tk

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

root = tk.Tk()


def get_webdata(website: str, **arg):
    r = requests.get(website, **arg)
    try:
        content = r.json()
    except json.decoder.JSONDecodeError:
        print('Niepoprawny format')
        return False
    else:
        return content


def get_picture(picture_website: str):
    web_picture = get_webdata(picture_website)
    picture_name = 'temp_picture.' + web_picture['file'][-3:]
    urllib.request.urlretrieve(web_picture['file'], picture_name)
    img = Image.open(picture_name).resize((700, 400))
    # img.show() #using default windows image browser
    return img


def main(websites: dict):

    website_img = get_picture(websites['picture'])
    web_text = get_webdata(websites['text'])

    tk_image = ImageTk.PhotoImage(website_img)
    label = tk.Label(None, text=web_text['text'], font=('Times', 18),
                     fg='blue', image=tk_image, compound='bottom', wraplength=700)
    label.grid(column=0, row=0, columnspan=3)

    add_buttons()

    root.mainloop()


def add_buttons():
    quit = tk.Button(text='QUIT', command=root.destroy)
    quit.grid(column=1, row=1,)

    next_cat = tk.Button(text='NEXT RANDOM CAT', command=show_cat)
    next_cat.grid(column=0, row=1,)

    next_dog = tk.Button(text='NEXT RANDOM DOG', command=show_dog)
    next_dog.grid(column=2, row=1,)


def show_cat():
    # root.destroy()
    main(cat_websites)


def show_dog():
    # root.destroy()
    main(dog_websites)


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
