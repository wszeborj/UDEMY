import requests
import json
from pprint import pprint


r = requests.get('https://jsonplaceholder.typicode.com/todos') #strona z danymi json
# r = requests.get('https://videokurs.pl') #strona bez danych json
# tasks = json.loads(r.text) #zamiana na stringa
# print(tasks)

def count_task_frequency(tasks):
    completed_taks_frequency_user = {}
    for entry in tasks:
        if(entry['completed'] ==  True):
            try:
                completed_taks_frequency_user[entry['userId']] += 1 
            except KeyError:
                completed_taks_frequency_user[entry['userId']] = 1
    return completed_taks_frequency_user

def get_keys_with_max_values(my_dict):
    return[
        key
        for key, value in my_dict.items()
        if value == max(my_dict.values())
    ]

def users_max_completed_tasks(completed_taks_frequency_user):
    best_users_completed_tasks = []
    max_amount_completed_tasks = max(completed_taks_frequency_user.values()) 
    for user_id, number_completed_task in completed_taks_frequency_user.items():
        if number_completed_task == max_amount_completed_tasks:
            best_users_completed_tasks.append(user_id)
    return best_users_completed_tasks


try:
    tasks = r.json()
    print(tasks)
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    completed_taks_frequency_user = count_task_frequency(tasks)
    best_users_completed_tasks = users_max_completed_tasks(completed_taks_frequency_user)
    print(completed_taks_frequency_user)
    print(f'Wreczamy ciasteczko mistrzunia osobom o id: {best_users_completed_tasks}.')


