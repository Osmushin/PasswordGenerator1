from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars_list = ''

print('Добро пожаловать в программу генерации безопасных паролей!')
print('Прежде чем я сгенерирую Вам самые лучшие пароли ответьте на несколько вопросов')

print('Введите необходимое количество паролей (это должно быть положительное число)')
amount = input()
print('Введите необходимое количество символов в одном пароле (это должно быть положительное число)')
long_digit = input()


def if_yesorno(answer, chars_list, spis):
    if answer in 'даДаДАнетНетНЕТ':
        if answer in 'даДаДА':
            chars_list += spis
            return True, print(chars_list)
        elif answer in 'нетНетНЕТ':
            return True, print('В вашем пароле не будут использованы цифры')
    else:
        return False

    print('Включать ли в состав пароля цифры? (ответьте "да" или "нет"')
    answerdigit = input()
    if if_yesorno(answerdigit, chars_list, digits) != True:
        answerdigit = input()




print('Включать ли в состав пароля маленькие буквы? (ответьте "да" или "нет"')
lowerletters = input()
print('Включать ли в состав пароля большие буквы? (ответьте "да" или "нет"')
upperletters = input()
print('Включать ли в состав пароля символы? (ответьте "да" или "нет"')
simbols = input()
print('Включать ли в состав пароля неоднозначные символы? (ответьте "да" или "нет"')
sim_simbols = input()
