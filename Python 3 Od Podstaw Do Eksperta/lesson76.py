user_file = r'C:\Users\user\OneDrive\Dokumenty\VisualStudioCode\nazwiskaaaa.txt'

try:
    with open(user_file, 'r', encoding='UTF-8') as file:
        print(file.read())
except FileNotFoundError:
    print('PLIK NIE ISTNIEJE')
