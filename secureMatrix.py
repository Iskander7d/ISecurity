"""
# Фролов Александр Леонидович КЭ-402
"""
from random import choice
users = [
    'Administrator',
    'Александр',
    'Владимир',
    'Глеб',
    'Сергей',
    'Анна',
    'Алексей',
    'Юрий'
]

objects = [
    'object1',
    'object2',
    'object3',
    'object4'
]

roots = {
    0: 'Запрет',
    1: 'Чтение',
    10: 'Запись',
    11: 'Чтение и Запись',
    101: 'Передача прав на Чтение',
    110: 'Передача прав на Запись',
    111: 'Полные права',
}

def is_include(object, value, is_dict = False):
    if is_dict:
        return value in object.values()
    else:
        return value in object


class User:
    def __init__(self):
        tmp_array = [i for i in roots]
        self.root = {key: choice(tmp_array) for key in objects}
        del tmp_array

    def show_roots(self):
        for object in objects:
            print('{:10} - {:10}'.format(object, roots[self.root[object]]))

    def give_root(self):

        if self.root < 100:
            print('Недостаточно прав на передачу\n')

        else:

            while True:
                object, granted_root, user = input('Объект, право, пользователь: ').split(' ')

                if not is_include(object, objects):
                    print('No such object')
                    continue
                if not is_include(granted_root, roots, 1):
                    print('No such root')
                    continue
                if not is_include(user, users):
                    print('No such user')
                    continue
                else:
                    break

            self_root = self.root[object]
            if self_root == 111:
                users[user].root[object] = granted_root

            elif (self_root | granted_root == self_root):
                users[user].root[object] = users[user].root[object] | granted_root
            else:
                print('Недостаточно прав на передачу')

    def use_file(self):

        operations = {
            1: 'read',
            10: 'write',
        }

        while True:
            object, operation = input('Файл, операция: ').split(' ')
            if not is_include(object, objects):
                print('No such object')
                continue
            if not operation in operations.values():
                print('No such operation')
                continue