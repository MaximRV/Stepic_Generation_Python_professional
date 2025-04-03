import json

fileName = input()
try:
    with open(fileName, 'r') as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print('Файл не найден')
except json.JSONDecodeError:
    print('Ошибка при десериализации')
