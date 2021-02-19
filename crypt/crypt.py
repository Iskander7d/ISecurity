
alphabet_eng = [chr(i) for i in range(97,123)]

def is_words_valid(text):
    tmp = ""
    A = list(text)
    Arr = []
    with open("dictionary.txt") as f:
        file = f.read().splitlines()
        for letter in A:
            if letter.isalpha():
                tmp += letter
            for word in file:
                if word == tmp:
                    Arr.append(tmp)
                    tmp = ""
                    break
        count = 0
        if len(Arr) == 0:
            return False
        for i in range(len(Arr)):
            if Arr[i] not in file or Arr[i] == "":
                return False
        return True

def checkTextWithDict(A,codename):
    tmp = ""  # Буффер для отделения слов от строки(т.к она приходит: втакомвиде)
    A = list(A)
    Arr = []  # хранение отделеных слов,которые прошли по словарю
    with open("dictionary.txt") as f:  # открываем словарь
        file = f.read().splitlines()  # Читаем все строки из словаря и с помощью .splitlines() избавляемся от \n
        for letter in A:  # проход по строке
            if letter.isalpha():  # если буква
                tmp += letter  # записываем её в буффер
            for word in file:  # Проверяем находится ли наш БУФФЕР СЛОВА в словаре
                if word == tmp:  # если да то добавляем в список Arr
                    Arr.append(tmp)
                    tmp = ""  # обнуляем буффер
                    break  # дальнейший проход по словарю не нужен
        count = 0
        if len(Arr) == 0:  # Если в этом списке пусто,значит ни одно слово не оказалось в словаре
            return False
        for i in range(len(Arr)):
            if Arr[i] not in file or Arr[i] == "":  # доп проверка,если слово не в словаре
                return False
        return "".join(A) + "\n\t\tDecoded with " + codename

def caesar_crypt(text, step=1):
    result = ''
    for symbol in text:
        symbol_index = alphabet_eng.index(symbol)
        if (symbol_index + step) < len(alphabet_eng):
            result += alphabet_eng[symbol_index + step]
        else:
            result += alphabet_eng[symbol_index + step - len(alphabet_eng)]

    return result

def caesar_encrypt(crypted_text, step=1):
    result = ''
    for symbol in crypted_text:
        symbol_index = alphabet_eng.index(symbol)
        if (symbol_index - step) >= 0:
            result += alphabet_eng[symbol_index - step]
        else:
            result += alphabet_eng[symbol_index - step + len(alphabet_eng)]
    return result, is_words_valid(result)

def vigenere_crypt(text, keyword):
    result = ''
    count = 0
    for symbol in text:
        symbol_index = alphabet_eng.index(symbol)
        if (symbol_index + alphabet_eng.index(keyword[count])) < len(alphabet_eng):
            result += alphabet_eng[symbol_index + alphabet_eng.index(keyword[count])]
        else:
            result += alphabet_eng[symbol_index - len(alphabet_eng) + alphabet_eng.index(keyword[count])]
        count += 1
        if count >= len(keyword):
            count = 0

    return result

def vigenere_encrypt(crypted_text, keyword):
    result = ''
    count = 0
    for symbol in crypted_text:
        symbol_index = alphabet_eng.index(symbol)
        if (symbol_index - alphabet_eng.index(keyword[count])) >= 0:
            result += alphabet_eng[symbol_index - alphabet_eng.index(keyword[count])]
        else:
            result += alphabet_eng[symbol_index - alphabet_eng.index(keyword[count]) + len(alphabet_eng)]
        count += 1
        if count >= len(keyword):
            count = 0

    return result, is_words_valid(result)


def playfair_crypt_encrypt(text, keyword_str, decoding=False):
    buffText = text
    Alphabet = alphabet_eng
    if "j" in Alphabet:   # удаляем j из-за особенностей шифра
        Alphabet.remove("j")
    keyword = list(keyword_str.lower())
    if "j" in keyword:
        keyword.remove("j")
    keyword = "".join(keyword)
    if "j" in text:
        text = list(text)
        text.remove("j")
        text = "".join(text)

    # Координаты х,y по значению value
    def coord(value, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if value == matrix[i][j]:
                    return str(i) + str(j)

    def encrypt(bigram):  # См комментарии к функции Code,все то же самое за исключением замены букв
        codeword = ""
        for bigr in bigram:
            x1 = int(coord(bigr[0], matrix)[0])
            y1 = int(coord(bigr[0], matrix)[1])
            x2 = int(coord(bigr[1], matrix)[0])
            y2 = int(coord(bigr[1], matrix)[1])
            if x1 == x2:  # Если элементы биграмы в одной строке
                try:
                    codeword += matrix[x1][y1 - 1]
                except:
                    codeword += matrix[x1][4]
                try:
                    codeword += matrix[x2][y2 - 1]
                except:
                    codeword += matrix[x2][4]
            elif y1 == y2:  # Если в одном столбце
                try:
                    codeword += matrix[x1 - 1][y1]
                except:
                    codeword += matrix[4][y1]
                try:
                    codeword += matrix[x2 - 1][y2]
                except:
                    codeword += matrix[4][y2]
            else:
                codeword += matrix[x1][y2]
                codeword += matrix[x2][y1]

        return codeword, is_words_valid(codeword)

    def crypt(bigram):
        codeword = ""  # хранение зашифрованного слова
        for bigr in bigram:
            x1 = int(coord(bigr[0], matrix)[0])  # Номер строки первой буквы
            y1 = int(coord(bigr[0], matrix)[1])  # Номер столбца первой буквы
            x2 = int(coord(bigr[1], matrix)[0])  #Номер строки второй буквы
            y2 = int(coord(bigr[1], matrix)[1])  #номер столбца второй буквы
            if x1 == x2:  # Если элементы биграмы в одной строке
                try:
                    codeword += matrix[x1][y1 + 1]  #Пытаемся заменить на след. в строке
                except:
                    codeword += matrix[x1][0]  #Если не получилось,означает ,что нужно заменить на 1 в строке
                try:
                    codeword += matrix[x2][y2 + 1]  #то же самое для второй буквы
                except:
                    codeword += matrix[x2][0]
            elif y1 == y2:  # Если в одном столбце
                try:
                    codeword += matrix[x1 + 1][y1]  #Заменить на ниже стоящий
                except:
                    codeword += matrix[0][y1]  #Если не вышло то на самый вехний
                try:
                    codeword += matrix[x2 + 1][y2]  #то же самое для 2 буквы
                except:
                    codeword += matrix[0][y2]
            else:
                codeword += matrix[x1][y2]  #Правила замены если разные столбцы и строки
                codeword += matrix[x2][y1]
        return codeword

    # Удалить повторы
    def removeRepeat(word):
        s = ""
        for letter in word:
            if letter not in s:
                s += letter
        return s

    Alphabet = removeRepeat(keyword + "".join(Alphabet))

    # Формируем матрицу
    matrix = []
    start = 0
    end = 5
    for i in range(5):
        matrix.append([])
        for j in range(start, end):
            matrix[i].append(Alphabet[j])
        start += 5
        end += 5

    # Проверяем биграмы на подряд идущие буквы и добавляем "х" куда нужно
    text = list(text)
    for i in range(0, len(text) - 1, 2):
        if text[i] == text[i + 1]:
            text.insert(i + 1, "x")
    if len(text) % 2:
        text.append("x")
    text = "".join(text)

    # Массив с биграммами
    bigrams = [[text[i], text[i + 1]] for i in range(0, len(text) - 1, 2)]   # создание биграмм
    if decoding:
        return encrypt(bigrams)
    else:
        return crypt(bigrams)

# %%
# Плейфер
def codeplayfair(text, decoding=False):
    buffText = text
    Alphabet = alphabet_eng
    if "j" in Alphabet:   # удаляем j из-за особенностей шифра
        Alphabet.remove("j")
    keyword = list("crypt".lower())
    if "j" in keyword:
        keyword.remove("j")
    keyword = "".join(keyword)
    if "j" in text:
        text = list(text)
        text.remove("j")
        text = "".join(text)

    # Координаты х,y по значению value
    def coord(value, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if value == matrix[i][j]:
                    return str(i) + str(j)

    # Дешифр текста
    def decode(bigram):  # См комментарии к функции Code,все то же самое за исключением замены букв
        codeword = ""
        for bigr in bigram:
            x1 = int(coord(bigr[0], matrix)[0])
            y1 = int(coord(bigr[0], matrix)[1])
            x2 = int(coord(bigr[1], matrix)[0])
            y2 = int(coord(bigr[1], matrix)[1])
            if x1 == x2:  # Если элементы биграмы в одной строке
                try:
                    codeword += matrix[x1][y1 - 1]
                except:
                    codeword += matrix[x1][4]
                try:
                    codeword += matrix[x2][y2 - 1]
                except:
                    codeword += matrix[x2][4]
            elif y1 == y2:  # Если в одном столбце
                try:
                    codeword += matrix[x1 - 1][y1]
                except:
                    codeword += matrix[4][y1]
                try:
                    codeword += matrix[x2 - 1][y2]
                except:
                    codeword += matrix[4][y2]
            else:
                codeword += matrix[x1][y2]
                codeword += matrix[x2][y1]
        return checkTextWithDict(codeword, "Playfair")

    # Кодирование текста
    def code(bigram):
        codeword = ""  # хранение зашифрованного слова
        for bigr in bigram:
            x1 = int(coord(bigr[0], matrix)[0])  # Номер строки первой буквы
            y1 = int(coord(bigr[0], matrix)[1])  # Номер столбца первой буквы
            x2 = int(coord(bigr[1], matrix)[0])  #Номер строки второй буквы
            y2 = int(coord(bigr[1], matrix)[1])  #номер столбца второй буквы
            if x1 == x2:  # Если элементы биграмы в одной строке
                try:
                    codeword += matrix[x1][y1 + 1]  #Пытаемся заменить на след. в строке
                except:
                    codeword += matrix[x1][0]  #Если не получилось,означает ,что нужно заменить на 1 в строке
                try:
                    codeword += matrix[x2][y2 + 1]  #то же самое для второй буквы
                except:
                    codeword += matrix[x2][0]
            elif y1 == y2:  # Если в одном столбце
                try:
                    codeword += matrix[x1 + 1][y1]  #Заменить на ниже стоящий
                except:
                    codeword += matrix[0][y1]  #Если не вышло то на самый вехний
                try:
                    codeword += matrix[x2 + 1][y2]  #то же самое для 2 буквы
                except:
                    codeword += matrix[0][y2]
            else:
                codeword += matrix[x1][y2]  #Правила замены если разные столбцы и строки
                codeword += matrix[x2][y1]
        return codeword

    # Оставить в тексте только буквы
    def delother(word):
        s = ""
        for letter in word:
            if letter.isalpha():
                s += letter
        return s

    # Удалить повторы
    def removeRepeat(word):
        s = ""
        for letter in word:
            if letter not in s:
                s += letter
        return s

    keyword = delother(keyword)   # оставить только буквы
    Alphabet = removeRepeat(keyword + "".join(Alphabet))  #убрать повторы
    text = delother(text)  #оставить только буквы

    # Формируем матрицу
    matrix = []
    start = 0
    end = 5
    for i in range(5):
        matrix.append([])
        for j in range(start, end):
            matrix[i].append(Alphabet[j])
        start += 5
        end += 5

    # Проверяем биграмы на подряд идущие буквы и добавляем "х" куда нужно
    text = list(text)
    for i in range(0, len(text) - 1, 2):
        if text[i] == text[i + 1]:
            text.insert(i + 1, "x")
    if len(text) % 2:
        text.append("x")
    text = "".join(text)

    # Массив с биграммами
    bigrams = [[text[i], text[i + 1]] for i in range(0, len(text) - 1, 2)]   # создание биграмм
    if decoding:
        return decode(bigrams)
    else:
        return code(bigrams)

# %%
# Проверка на нахождение слов внутри словаря
def checkTextWithDict(A,codename):
    tmp = ""  # Буффер для отделения слов от строки(т.к она приходит: втакомвиде)
    A = list(A)
    Arr = []  # хранение отделеных слов,которые прошли по словарю
    with open("dictionary.txt") as f:  # открываем словарь
        file = f.read().splitlines()  # Читаем все строки из словаря и с помощью .splitlines() избавляемся от \n
        for letter in A:  # проход по строке
            if letter.isalpha():  # если буква
                tmp += letter  # записываем её в буффер
            for word in file:  # Проверяем находится ли наш БУФФЕР СЛОВА в словаре
                if word == tmp:  # если да то добавляем в список Arr
                    Arr.append(tmp)
                    tmp = ""  # обнуляем буффер
                    break  # дальнейший проход по словарю не нужен
        count = 0
        if len(Arr) == 0:  # Если в этом списке пусто,значит ни одно слово не оказалось в словаре
            return False
        for i in range(len(Arr)):
            if Arr[i] not in file or Arr[i] == "":  # доп проверка,если слово не в словаре
                return False
        return "".join(A) + "\n\t\tDecoded with " + codename

# %%
# Разбиваем текст на слова
def splitText(text):
    sText = []
    word = ""
    for letter in text:
        if letter in alphabet_eng:  # избавляемся от знаков препинания
            word += letter
        else:
            sText.append(word)  # если встретился знак препинания,то добавляем его в список
            sText.append(letter)
            word = ""
    if word:  # если строка кончилась не знаком препинания,то добавляем последнее слово
        sText.append(word)
    return sText

def main():
    input_data = input('Введите текст для шифровки/дешифровки: ')
    print(input_data)
    print('C - Шифр Цезаря\nV - Шифр Вижинера\nP - Шифр Плейфера\n')
    while True:
        print('1)Закодировать\n2)Декодировать\n3)Выйти\n>>>')
        choice = input()
        choice = int(choice)
        if choice == 1:
            cypher = input('Шифр: ')
            if cypher == 'C':
                result = caesar_crypt(input_data, 3)
                print(result)
                break
            if cypher == 'V':
                result = vigenere_crypt(input_data, 'crypt')
                print(result)
                break
            if cypher == 'P':
                result = playfair_crypt_encrypt(input_data, 'crypt')
                print(result)
                break
        if choice == 2:
            print(caesar_encrypt(input_data, 3))
            print(vigenere_crypt(input_data, 'crypt'))
            print(playfair_crypt_encrypt(input_data, 'crypt', True))
        if choice == 3:
            break

if __name__ == '__main__':
    main()