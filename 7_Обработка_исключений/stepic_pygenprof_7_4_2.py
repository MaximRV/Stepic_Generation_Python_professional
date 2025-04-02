
def get_id(names: list, name:str):
    if not isinstance(name,str):
        raise TypeError('Имя не является строкой')
    if not name.isalpha() or not name.istitle():
        raise ValueError('Имя не является корректным')
    newStudentId = len(names) + 1

    return newStudentId



names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))