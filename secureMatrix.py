"""
# Фролов Александр Леонидович КЭ-402
"""
from random import choice


class User:
    def __init__(self):
        tmp_array = [i for i in roots]
        self.root = {key: choice(tmp_array) for key in objects}
        del tmp_array

    def show_roots(self):
        for object in objects:
            print('{:10} - {:10}'.format(object, roots[self.root[object]]))

    def grant_root(self):

        if self.root[object] < 100:
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
                if not is_include(user, usernames):
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
            'read': 1,
            'write': 10
        }

        while True:
            object, operation = input('Объект, операция: ').split(' ')

            if not is_include(object, objects):
                print('No such object')
                continue
            if not operation in operations.keys():
                print('No such operation')
                continue

            self_root = self.root[object]
            if self_root | operations[operation] == self_root:
                print('Операция проведена успешно')
                break
            else:
                print('Недостаточно прав на {} для {}'.format(operation, object))
                break



usernames = [
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

users = [User() for i in usernames]


def is_include(value, object, is_dict=False):
    if is_dict:
        return value in object.values()
    else:
        return value in object

def login(name):
    if name in usernames:
        return True
    return False

def main():
    while True:
        command = input('>>>').lower()
        if command == "login":
            name = input("Имя пользователя: ")
            if login(name):
                user = users[usernames.index(name)]
                while True:
                    command = input('>>>').lower()
                    if command == "roots":
                        user.show_roots()
                    if command == "grant":
                        user.grant_root()
                    if command == "file":
                        user.use_file()
                    if command == "logout":
                        break
            else:
                break
        if command == "quit":
            break

if __name__ == '__main__':
    main()