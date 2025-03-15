
file_name = input()
try:
    with open(file_name, 'r', encoding= 'utf-8' ) as file:
            print(file.read())
except:
    print('Файл не найден')