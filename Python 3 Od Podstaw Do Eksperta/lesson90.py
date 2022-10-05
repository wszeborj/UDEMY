import requests


import requests
import json
import webbrowser
from pprint import pprint
from datetime import datetime, timedelta

'''
za pomoca API pobieramy pytania ze strony stackoverflow ktore muszą spełnic nastepujace warunki:
minimalnie 15 punktow
posegregowane malejaco
z ostatniego tygodnia
kategorii python
'''
print(timedelta(days=10))
print(datetime.today())
search_date = datetime.today() - timedelta(days=10)

params = {
    'site': 'stackoverflow',
    'sort': 'votes',
    'order': 'desc',
    'fromdate': int(search_date.timestamp()),
    'tagged': 'python',
    'min': 10

}

r = requests.get('https://api.stackexchange.com/2.3/questions/', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    for question in questions['items']:
        webbrowser.open_new_tab(question['link'])
