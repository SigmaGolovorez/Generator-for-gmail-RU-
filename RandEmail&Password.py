from random import *
from secrets import *
from string import *

letters = ascii_letters
lowerletters = ascii_lowercase
digits = digits
specsymbol = punctuation
alphabet = letters + digits + specsymbol
lettersgroup = lowerletters + digits
pwd = ''
email = ''
maillen = randint(10, 30)

print("Здравствуйте, это программа для создания почты и пароля гугл")
while True:
    ans = input("Хотите ли вы вставить какое-нибудь слово в почту(да,нет)?\n")
    if ans.lower() == 'да':
        valid = False
        while not valid:
            word = input("Напишите что хотите вставить \n(на английском языке нижним регистром и/или число, без пробелов и специальных символов не короче 1 символа и не длиннее 20 символов)\n")
            valid = True
            if len(word) > 20:
                print("Слишком длинное слово")
                valid = False
            elif len(word) == 0:
                print("Слово не может быть пустым")
                valid = False
            else:
                for symbol in word:
                    if symbol not in lettersgroup:
                        print(f"Символ {symbol} не подходит")
                        valid = False
                        break

            if valid:
                for i in range(7):
                    word += choice(lettersgroup)
                mail = word + '@gmail.com'
        break
    elif ans.lower() == 'нет':
        for i in range(maillen):
            email += choice(lettersgroup)
        email += '@gmail.com'
        break
    else:
        print("Ответ неверный")
while True:
    ans = input('Хотите ли вы сами придумать длину пароля(0) или выбрать рандомно(1)?\n')
    if ans == '0':
        while True:
            pwdlen = int(input("Введите длину пароля(от 8 до 12):"))
            if pwdlen < 8 or pwdlen > 12:
                print("Ответ неверный")
            else:
                print("Число принято")
                break
        break
    elif ans == '1':
        pwdlen = randint(8, 12)
        break
    else:
        print("Ответ неверный")
for i in range(pwdlen):
    pwd += choice(alphabet)
print(f'Ваша новая почта-{email}\nВаш новый пароль-{pwd}')