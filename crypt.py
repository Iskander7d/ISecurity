
alphabet_eng = [chr(i) for i in range(97,123)]

def is_words_valid(text):
    tmp = ""  # Буффер для отделения слов от строки(т.к она приходит: втакомвиде)
    A = list(text)
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
        return True


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


def main():

    default = 'toand'
    crypted= caesar_crypt(default)
    encrypted, is_valid = caesar_encrypt(crypted)

    print(crypted, encrypted, is_valid)

if __name__ == '__main__':
    main()