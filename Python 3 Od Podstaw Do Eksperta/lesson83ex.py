import requests
import json

'''ze strony internetowej na ktorej znajduja sie przykladowe dane w formacie json
wydobac informacje kto wykonal najwiecej zadan'''


def task_user_dict_from_web_json(web_address:str) -> dict:
    '''download json data from website and convert it to dictionary'''
    all_tasks_dict = 0
    try:
        first_data_object = requests.get(web_address)
    except requests.exceptions.ConnectionError:
        print('Can not download data from website: {web_address}')
    else:
        complete_data_string = first_data_object.text
        # all_tasks_dict = json.loads(complete_data_string)
        try:
            all_tasks_dict = complete_data_string.json() #przy okazji sprawdza poprawnosc
        except json.decoder.JSONDecodeError:
            print('Wrong format')
        else:
            return all_tasks_dict


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
    best_users_list = [
                      key 
                      for key, value in user_completed_tasks_dict.items()
                      if value == max(user_completed_tasks_dict.values())
                      ]

    # for key, value in user_completed_tasks_dict.items():
    #     if value == max(user_completed_tasks_dict.values()):
    #         best_users.append(key)
    return best_users_list




if __name__ == '__main__':
    todos_web_address = r'https://jsonplaceholder.typicode.com/todos'
    all_tasks_dict = task_user_dict_from_web_json(todos_web_address)
    if all_tasks_dict:
        user_completed_tasks_dict = sum_completed_tasks_by_users(all_tasks_dict)
        best_users_list = get_best_users_id(user_completed_tasks_dict)
        print(f'The most completed tasks were performed by users: {best_users_list}.')
    else:
        print('Something went wrong. Check connection or correct data')
    



