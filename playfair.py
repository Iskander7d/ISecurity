alphabet_eng = [chr(i) for i in range(97,123)]

def is_words_valid(codeword):
    pass

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