#!/usr/bin/env python3

import string
import random

root_password = ''.join([chr(random.randint(33, 126)) for x in range(40)]).encode()

print(root_password)

with open('./flag', 'rb') as f:
    flag = f.read().strip()

print('Welcome, Here is a resposible login system, enter password for access!')

for i in range(400):
    guess = input('> ').encode()
    if guess == root_password:
        print('Congratulations !')
        print('flag = %s' % flag)
        break

    password_int = int.from_bytes(root_password, 'big')
    guess_int = int.from_bytes(guess, 'big')
    if guess_int > password_int:
        print('Wroooooog password, tooooooo big!')
    else:
        print('Wroooooog password, tooooooo small!')
else:
    print('Toooooo many failed attempts, account locked!')
