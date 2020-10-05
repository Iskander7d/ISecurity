# %%
"""
# Кашафеев Вячеслав Рамазанович КЭ-204
"""

# %%
from random import choice  # для случайного заполнения прав

# %%
class User:  #  класс пользователя
    def __init__(self):  # конструктор
        arr = [i for i in roots]  # массив с бинарными правами т.к random.choice() работает только со списками
        self.root = {key: choice(arr) for key in objects}  #  кортеж Ключ:Имя файла,Значение:Случайные права
        del arr  #  ОПТИМИЗАЦИЯ...удаляем ненужный массив

    def showRoots(self):  # вывести права на экран(пользователя который вошел в систему)
        k = 1
        for file in objects:  # objects - имена файлов
            print(str(k) + "){:10}".format(file + ":") + "{:10}".format(roots[self.root[file]]))
            k += 1
        print(30 * "*")

    def giveRoot(self):  # передать права(от пользователя который вошел в систему)
        while True:  # Выбор файла на который передаются права
            filename = input("На какой файл передаются права: ").lower()
            if filename.isdigit():  # если файл выбран номером
                if (0 > int(filename)) or (int(filename) > len(objects)) or (not int(filename)):
                    print("Неверно выбран файл.Попробуйте ещё раз.")
                    continue
                else:  # если файл выбран названием
                    filename = int(filename) - 1
            filename = objects[int(filename)]
            if isInclude(objects, filename):  # проверяем существует ли такой файл
                break  # выходим из цикла,выбор файла успешен
            else:
                print("Ошибка ввода данных.Попробуйте еще раз.")
        while True:  # выбор права для передачи 
            root = input("Какое право передается(Чтение,Запись): ")
            if isInclude(roots, root, 1):  # существует ли такое право
                root = getKey(roots, root) # переходим от текстового к бинарному обозначению права
                break  # выходим из цикла,право выбрано успешно
            else:
                print("Ошибка ввода данных.Попробуйте еще раз.")
        while True:  # выбор пользователя кому передаем права
            name = input("Кому вы хотите это передать: ")
            if isInclude(usernames, name):  # проверяем существует ли такой пользователь
                name = usernames.index(name.lower())
                break # выход из цикла,пользователь выбран успешно
            else:
                print("Ошибка ввода данных.Попробуйте еще раз.")
        if (self.root[filename] > 100) or (self.root[filename] == root):  # Проверяем может ли пользователь передать такое право
            users[name].root[filename] = users[name].root[filename] | root

    def useFile(self): # работа с файлом(не передача)
        while True:  # выбираем файл для работы
            filename = input("Выберите файл: ").lower()
            if filename.isdigit():  # если файл выбран номером
                if (0 > int(filename)) or (int(filename) > len(objects)) or (not int(filename)):
                    print("Неверно выбран файл.Попробуйте ещё раз.")
                    continue
                else:
                    filename = int(filename) - 1
            filename = objects[int(filename)]  # переходим от цифрового обозначения к текстовому
            if isInclude(objects, filename):  # существует ли такой файл
                break  # выход из цила,файл выбран успешно
            else:
                print("Ошибка ввода данных.Попробуйте еще раз.")
        while True:  # выбираем действие
            root = input("Действие над " + filename + ":")
            if isInclude(roots, root, 1):  # существует ли такое действие
                root = getKey(roots, root) # переходим от текстового к бинарному обозначению права
                break  # выход из цикла,право выбрано успешно
            else:
                print("Ошибка ввода данных.Попробуйте еще раз.")
        if self.root[filename] % 2:  # Может ли пользователь совершить Выбранное действие над Выбранным файлом
            print("Вы успешно провели" + roots[root] + " " + filename)
        else:
            print("У вас недостаточно прав для " + roots[root] + " " + filename)

# %%
usernames = ["дарья",
             "азат",
             "дмитрий",
             "максим",
             "виктор",
             "вячеслав",
             "полина",
             ] # Имена пользователей
roots = {0: "Запрет",
         1: "Чтение",
         10: "Запись",
         11: "Чтение и Запись",
         101: "Чтение - Передача прав",
         110: "Запись - Передача прав",
         1000: "Запись,Чтение - Передача прав",
         1001: "Чтение,Запись - Передача прав",
         111: "Полные права",
         } # бинарное обозначение прав
objects = ["файл 1", "файл 2", "файл 3", "файл 4"] # имена файлов
users = [User() for i in usernames] # список экземпляров класса длиной в количество пользователей


# %%
def login(logName):  # Функция для логина,3 попытки на вход, если Ошибка входа - прекращение программы
    count = 2  # счетчик попыток
    while count:
        for currentName in usernames:  # правильное ли ввели имя
            if logName == currentName.lower():
                print("Вход успешно выполнен.")
                return True # успех,выход из функции
        print("Ошибка ввода данных.")
        count -= 1
        logName = input("Имя пользователя:")
    print("Вы использовали все попытки входа.")
    return False # ошибка ввода,выход из функции

# %%
def getKey(dictionary, value):  # Возвращает ключ из словаря dictionary по значению value
    if len(dictionary) > 0:
        for item in dictionary:
            if dictionary[item] == value:
                return item
    return None

# %%
def isInclude(array, value, dictvalue=0):  # Проверяем есть ли элемент в списке или элемент из кортежа
    if dictvalue: # dictvalue:  1 - Кортеж, 0 - список
        for element in array:
            if array[element] == value:
                return True
    else:
        for element in array:
            if element == value:
                return True
    return False

# %%
def adminsRoots():  # рандом права и админку мне
    for fileName in objects:  # админку мне
        users[usernames.index("вячеслав")].root[fileName] = 111  # Админку мне;
        users[usernames.index("дарья")].root[fileName] = 0  # запрет на все файлы,для тестов

# %%
def main():
    adminsRoots()  # Админка и Одному челику все запреты для тестов
    while True:  # бесконечный цикл для ввода команд
        command = (str(input(">>>"))).lower()
        if command == "вход":  # Команда для входа в систему
            name = str(input("Имя пользователя:")).lower()
            if login(name):
                while True:
                    command = (str(input(">>"))).lower()
                    if command == "показать права":
                        users[usernames.index(name.lower())].showRoots()
                    if command == "передать право":
                        users[usernames.index(name.lower())].giveRoot()
                    if command == "файлы":
                        users[usernames.index(name.lower())].useFile()
                    if (command == "выход") or (command == "завершить"):
                        break
            else:
                break
        if command == "завершить":  # Выход из программы
            break

# %%
if __name__ == '__main__':
    main()