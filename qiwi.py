from SimpleQIWI import *
import os
yellow='\033[33m'
red='\033[31m'
green='\033[32m'
white='\033[37m'
import random 
from random import randint
def pay():
    token=input('токен: ')
    phone=''
    os.system('clear')
    try:
        api=QApi(token=token, phone=phone)
    except:
        print('\033[33m[-]неверный токен или ваш IP заблокир0ван')
    print('[+]токен ',token)
    print('[$]баланс ',api.balance[0],' рублей')
    print('---')
    print('[1] - обновить баланс Qiwi\n[2] - перевести на другой Qiwi\n[3] - изменить токен\n[4] - добавить  токен в сохраненные\n[5] - показать сохраненные токены')
    balance=api.balance[0]
    while True:
        payment=input(': ')
        if payment=='1':
            print('[$]баланс ',balance)
        elif payment=='2':
            print('пример номера +7 999 555 45 67')
            my_number=input('qiwi получателя: ')
            bay=input('сколько перевести: ')
            try:
                api.pay(account=my_number,amount=bay,comment='termux legacy')
                print(green+'переведенно '+bay+' рублей'+white)
            except:
                print(red+'не переведенно'+white)
        elif payment=='3':
            pay()
        elif payment=='4':
            print('токен для сохранения')
            toks=input(': ')
            l=open(u"save_token.txt", 'a')
            l.write(toks+'\n')
            l.close()
            print('сохраненно')
        elif payment=='5':
            k=open("save_token.txt", 'r')
            k.read()
            print(k)
            k.close()
        
try:
    pay()
except:
    print('\n'+yellow+'ошибка доступа\nповторите позже')
