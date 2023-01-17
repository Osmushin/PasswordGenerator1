from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
noneonesimbols = 'il1Lo0O'
chars = []


# Функция проверки ответа пользователя на число
def is_digit(digit):
    if digit.isdigit():
        if int(digit) >= 1:
            return True
        else:
            return False
    else:
        return False


# Функция проверки ответа на да и нет
def word_yesorno(answer):
    if answer in 'даДаДАнетНетНЕТ':
        return True
    else:
        return False


# Функция проверки Да или Нет и внесение симолов в массив chars
def yesorno(answer, simbols):
    if answer in 'даДаДА':
        return chars.extend(simbols)
    elif answer in 'нетНетНЕТ':
        return False


# Функция генерации паролей
def generate_password(length, chars):
    password = []
    for i in range(1, length + 1):
        password.append(chars[randint(0, len(chars))])
    return password


print('Добро пожаловать в программу генерации безопасных паролей!')
print('Прежде чем я сгенерирую Вам самые лучшие пароли ответьте на несколько вопросов')

print('Введите необходимое количество паролей (это должно быть целое положительное число)')
amount = input()
while not is_digit(amount):
    print('Это должно быть целое положительное число')
    amount = input()

print('Введите необходимое количество символов в одном пароле (это должно быть положительное число)')
long_digit = input()
while not is_digit(long_digit):
    print('Это должно быть целое положительное число')
    long_digit = input()

print('Включать ли в состав пароля цифры? (ответьте "да" или "нет")')
answerdigit = input()
while not word_yesorno(answerdigit):
    print('ответьте "да" или "нет"')
    answerdigit = input()
yesorno(answerdigit, digits)

print('Включать ли в состав пароля маленькие буквы? (ответьте "да" или "нет")')
lowerletters = input()
while not word_yesorno(lowerletters):
    print('ответьте "да" или "нет"')
    lowerletters = input()
yesorno(lowerletters, lowercase_letters)

print('Включать ли в состав пароля большие буквы? (ответьте "да" или "нет")')
upperletters = input()
while not word_yesorno(upperletters):
    print('ответьте "да" или "нет"')
    lowerletters = input()
yesorno(upperletters, uppercase_letters)

print('Включать ли в состав пароля символы? (ответьте "да" или "нет")')
simbols = input()
while not word_yesorno(simbols):
    print('ответьте "да" или "нет"')
    simbols = input()
yesorno(simbols, punctuation)

print('Включать ли в состав пароля неоднозначные символы (il1Lo0O)? (ответьте "да" или "нет")')
sim_simbols = input()
while not word_yesorno(sim_simbols):
    print('ответьте "да" или "нет"')
    sim_simbols = input()
if sim_simbols in "нетНетНЕТ":
    for i in range(len(noneonesimbols)):
        chars.remove(noneonesimbols[i])

for i in range(1, int(amount)+1):
    print('Пароль №', i, ':', end='')
    print(*generate_password(int(long_digit), chars), sep='')

print('Спасибо за использование нашего генератора паролей!')