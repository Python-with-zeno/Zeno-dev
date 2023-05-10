# A kis appról készült felvétel itt érhető el:  https://drive.google.com/file/d/1IUCqaOgdGfFTt6vvgnjv0-bFg66dCM_V/view?usp=share_link

import random

#               0       1       2
kopapirollo = ['kő' ,'papír' ,'olló']

print('\n')
print('='*22)
print('Üdvözöllek a játékban!')
print('='*22)
print('\n')

# legközelebb átírjuk a tömb használatára
user = input('Válassz egyet a 3 közül! ')

if user != "kő" or user != "papír" or user != "olló":
    print('Nem megfelelő választás!')
    exit()

ellenfel_num = random.randint(0,2)

if ellenfel_num == 0:
    ellenfel = 'kő'
if ellenfel_num == 1:
    ellenfel = 'papír'
if ellenfel_num == 2:
    ellenfel = 'olló'


print("A user:", user, "az ellenfél:", ellenfel)

if user == 'kő' and ellenfel == 'papír':
    print('ellenfél nyert.')
if user == 'kő' and ellenfel == 'olló':
    print('user nyert.')
if user == 'kő' and ellenfel == 'kő':
    print('döntetlen.')

if user == 'papír' and ellenfel == 'papír':
    print('döntetlen.')
if user == 'papír' and ellenfel == 'olló':
    print('ellenfél nyert.')
if user == 'papír' and ellenfel == 'kő':
    print('user nyert.')

if user == 'olló' and ellenfel == 'papír':
    print('user nyert.')
if user == 'olló' and ellenfel == 'olló':
    print('döntetlen.')
if user == 'olló' and ellenfel == 'kő':
    print('ellenfél nyert')







