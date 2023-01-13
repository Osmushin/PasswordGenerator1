from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars_list = ''


# Функция проверки на число
def is_digit(digit):
    if digit.isdigit():
        if int(digit) >= 1:
            return True
        else:
            return False
    else:
        return False



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



print('Включать ли в состав пароля цифры? (ответьте "да" или "нет"')
answerdigit = input()


print('Включать ли в состав пароля маленькие буквы? (ответьте "да" или "нет"')
lowerletters = input()
print('Включать ли в состав пароля большие буквы? (ответьте "да" или "нет"')
upperletters = input()
print('Включать ли в состав пароля символы? (ответьте "да" или "нет"')
simbols = input()
print('Включать ли в состав пароля неоднозначные символы? (ответьте "да" или "нет"')
sim_simbols = input()
