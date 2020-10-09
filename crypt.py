
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


def playfair_crypt():
    pass

def playfair_encrypt():
    pass

def main():

    default = 'intheend'
    keyword = 'hello'
    crypted = vigenere_crypt(default, keyword)
    encrypted, is_valid = vigenere_encrypt(crypted, keyword)
    print(crypted, encrypted, is_valid)

if __name__ == '__main__':
    main()