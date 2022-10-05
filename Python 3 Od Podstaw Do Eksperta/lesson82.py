import requests
import json
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pprint import pprint


def read_file_return_list() -> tuple:
    webs_file = askopenfilename()
    # webs_file = r"C:\Users\user\OneDrive\Dokumenty\VisualStudioCode\websites.txt"
    status = False
    try:
        with open(webs_file, 'r', encoding='UTF-8') as file:
            webs_list = list(file.read().split())
            status = True
    except:
        print('Cannot read file!!')
        status = False
    finally:
        return status, webs_list


def check_web_list(webs_list: list) -> dict:
    webs_response_dict = {}
    status = False

    for web in webs_list:
        try:
            web_response = requests.get(web)
            if web_response.status_code == 200:
                status = True
        except requests.exceptions.ConnectionError:
            status = False
        finally:
            webs_response_dict[web] = status
    pprint(webs_response_dict)
    return webs_response_dict


def save_web_response_list(webs_response_dict):
    checked_webs_file = asksaveasfilename()
    webs_response_string = json.dumps(webs_response_dict, ensure_ascii=False)
    try:
        with open(checked_webs_file, 'w') as file:
            file.write(webs_response_string)
        print('File ', checked_webs_file, ' - SAVED')
        return True
    except:
        print('Could not save file')
        return False


def show_original_content() -> None:
    file_name = askopenfilename()
    print(f'Show original content of file {file_name}')
    with open(file_name, 'r', encoding='UTF-8') as file:
        string_file = file.read()
    pprint(string_file)


def show_content_json() -> None:
    json_file_name = askopenfilename()
    print(f'Show content of json file {json_file_name}')
    with open(json_file_name, 'r', encoding='UTF-8') as json_file:
        string_json = json.load(json_file)
    pprint(string_json)


if __name__ == '__main__':
    status, webs_list = read_file_return_list()
    if status:
        checked_webs_dict = check_web_list(webs_list)
        saved = save_web_response_list(checked_webs_dict)
        if saved:
            show_original_content()
            show_content_json()

