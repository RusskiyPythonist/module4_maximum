def IsPolidrome(word: str):
    if word[::-1] == word:
        return True
    else:
        return False


if __name__ == '__main__':
    word = input('Введите слово: ')
    print(IsPolidrome(word))
