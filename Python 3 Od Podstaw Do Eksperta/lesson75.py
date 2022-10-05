
namesAndSurnames = []

with open (r'C:\Users\user\OneDrive\Dokumenty\VisualStudioCode\imionanazwiska.txt', 'r', encoding='UTF-8') as file:
    # print(file.read())
    # print(file.tell())
    for line in file:
        namesAndSurnames.append(tuple(line.split()))

print(namesAndSurnames)

with open (r'C:\Users\user\OneDrive\Dokumenty\VisualStudioCode\imiona.txt', 'w', encoding='UTF-8') as file:
    for item in namesAndSurnames:
        file.write(item[0] + '\n')

with open (r'C:\Users\user\OneDrive\Dokumenty\VisualStudioCode\nazwiska.txt', 'w', encoding='UTF-8') as file:
    for item in namesAndSurnames:
        try :
            file.write(item[1] + '\n')
        except IndexError:
            file.write('\n')