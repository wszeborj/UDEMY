import requests
import json
from collections import defaultdict


'''put in dictionary default value, thanks to that you do 
not have to use try/except in function sum_completed_tasks_by_users'''
test_dict = defaultdict(int) 
print("test_dict['userId'] = ", test_dict['userId'])

'''ze strony internetowej na ktorej znajduja sie przykladowe dane w formacie json
wydobac informacje kto wykonal najwiecej zadan'''


def dict_from_web_json(web_address:str) -> dict:
    '''download json data from website and convert it to dictionary'''
    try:
        org_web_data = requests.get(web_address)
    except requests.exceptions.ConnectionError:
        print('Can not download data from website: {web_address}')
    else:
        # complete_data_string = first_data_object.text
        # all_tasks_dict = json.loads(complete_data_string)
        try:
            web_data_dict = org_web_data.json() #przy okazji sprawdza poprawnosc
        except json.decoder.JSONDecodeError:
            print('Wrong format')
        else:
            return web_data_dict


def sum_completed_tasks_by_users(all_tasks_dict: dict) -> dict:
    '''from dictionary get user id and sum of completed tasks'''
    user_completed_tasks_dict = {}

    for task in all_tasks_dict:
        if task['completed'] == True:
            userID = task['userId']
            try:
                user_completed_tasks_dict[userID] = user_completed_tasks_dict[userID] + 1
            except:
                user_completed_tasks_dict[userID] = 1
    return user_completed_tasks_dict


def get_best_users_id(user_completed_tasks_dict:dict) -> list:
    '''from dict[userID]=sum_of_completed_task 
    get user Id which have the most completed tasks'''

    best_users = []
    best_users_id_list = [
                      key 
                      for key, value in user_completed_tasks_dict.items()
                      if value == max(user_completed_tasks_dict.values())
                      ]

    # for key, value in user_completed_tasks_dict.items():
    #     if value == max(user_completed_tasks_dict.values()):
    #         best_users.append(key)
    return best_users_id_list

def find_names_by_id(best_users_id_list: list, users_data_dict: dict) -> list:

    best_users_name_list = []
    for user in users_data_dict:
        if user['id'] in best_users_id_list:
            best_users_name_list.append(user['name'])
    # print(f'The most completed tasks were performed by users: {best_users_name_list}.')
    # best_users_name_list2 = [user['name'] for user in users_dict if user['id'] in best_users_id_list]
    # print(f'The most completed tasks were performed by users: {best_users_name_list2}.')
    return best_users_name_list


if __name__ == '__main__':
    todos_web_address = r'https://jsonplaceholder.typicode.com/todos'
    all_tasks_dict = dict_from_web_json(todos_web_address)
    if all_tasks_dict:
        user_completed_tasks_dict = sum_completed_tasks_by_users(all_tasks_dict)
        best_users_id_list = get_best_users_id(user_completed_tasks_dict)
        print(f'The most completed tasks were performed by users: {best_users_id_list}.')
    else:
        print('Something went wrong. Check connection or correct data')
    
    # case 1: pobieramy cala zawartosc strony
    users_web_address = r'https://jsonplaceholder.typicode.com/users'
    users_data_dict = dict_from_web_json(users_web_address)
    # print(users_data_dict)
    if users_data_dict:
        best_users_name_list = find_names_by_id(best_users_id_list, users_data_dict)
        print(f'Case1:The most completed tasks were performed by users: {best_users_name_list}.')
    
    # case 2: pobieramy kolejno tylko jednego usera o konkretnym id
    best_users_name_list2 = []

    for user_id in best_users_id_list:
        users_web_address = r'https://jsonplaceholder.typicode.com/users/' + str(user_id) #it will return one dictionary
        users_data_dict = dict_from_web_json(users_web_address) # everytime when it connect it take time
        best_users_name_list2.append(users_data_dict['name'])

    print(f'Case2:The most completed tasks were performed by users: {best_users_name_list2}.')

    # case 2.5: pobieramy kolejno tylko jednego usera o konkretnym id
    best_users_name_list2_5 = []

    for user_id in best_users_id_list:
        # everytime when it connect it take time
        org_users_web_data = requests.get('https://jsonplaceholder.typicode.com/users', params='id=' + str(user_id)) #it will return list of dictionary
        users_data_dict = org_users_web_data.json()
        best_users_name_list2_5.append(users_data_dict[0]['name'])
        
    print(f'Case2.5:The most completed tasks were performed by users: {best_users_name_list2_5}.')

    # case 3: pobieramy wiele rekordow
    best_users_name_list3 = []

    key = 'id'
    key_eq = key + '='
    for index, user_id in enumerate(best_users_id_list):
        if index == 0:
            params = key_eq + str(best_users_id_list[0])
        else:
            params = params + '&' + key_eq + str(user_id)

    # org_users_web_data = requests.get('https://jsonplaceholder.typicode.com/users', params='id=5&id=10') 
    org_users_web_data = requests.get('https://jsonplaceholder.typicode.com/users', params=params) 
    users_data_list_of_dict = org_users_web_data.json()

    for user in users_data_list_of_dict:
        best_users_name_list3.append(user['name'])

    print(f'Case3:The most completed tasks were performed by users: {best_users_name_list3}.')




        

    



