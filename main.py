from random import randint as r
from os import system as s

chars = ('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

def create_pass():
    n = int(input('Введите количество знаков пароля: '))
    password = ''
    for i in range(n):
        password = f'{password}{chars[r(0, len(chars) - 1)]}'

    print(password)


prog = True

while prog:
    create_pass()
    k = input("Ввести новый пароль? (y/n) : ")
    if k == 'y':
        prog = True
    else:
        prog = False
    s("cls")
