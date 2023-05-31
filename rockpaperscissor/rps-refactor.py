import random

#               0       1       2
kopapirollo = ['kő' ,'papír' ,'olló']

print('\n')
print('='*22)
print('Üdvözöllek a játékban!')
print('='*22)
print('\n')

# legközelebb átírjuk a tömb használatára
user_num = input('Válassz egyet a 3 közül! (0 = kő, 1 = papír, 2 = olló): ')

# ez egy függvény, amit hiba esetén futtattunk
def hiba():
    print('Nem megfelelő választás!')
    exit()

# a try: except: blokkot használjuk, hogy a program ne álljon le, ha a user nem számot ad meg, vagy nem megfelelő számot ad meg
# a try, mint a próbálkozás, a except pedig a kivétel, amit a try blokkban megadunk, olyan mintha gondoltaben futtatná a kódunkat, és ha nincs hiba, akkor a try blokk fut le, ha van, akkor a except blokk fut le
try:
    user_num = int(user_num)
except:
    hiba()
    
if int(user_num) >= len(kopapirollo):
    hiba()
    
user = kopapirollo[user_num]

#itt ahelyett, hogy ifekkel ellenőriznénk, hogy mi a user választása, egyszerűen a tömbből kivesszük a választott elemet
# és hogy a véetlen számunk is dinamikusan a tömb tartalmától függjön, a tömb hosszát vesszük alapul, ezzel a kifejezéssel: len(kopapirollo)-1
# a -1 azért szükséges, mert a tömbünk 3 darab elemet tartalmaz, de a tömb indexelése 0-tól kezdődik, így a 3. elem indexe 2 lesz, és nekünk indexre van szükségünk, hogy megszólítsuk az adott elemet
ellenfel_num = random.randint(0, len(kopapirollo)-1)
ellenfel = kopapirollo[ellenfel_num]

print("A user:", user, "az ellenfél:", ellenfel)


#                 0       1       2
# kopapirollo = ['kő' ,'papír' ,'olló']

# ez a függvény matematikailag megoldja, hogy ki nyert
# egymást kizáró feltétlek vannak, tehát ha az egyik feltétel teljesül, akkor a többi nem fog lefutni
# van egy speciális esetünk, amikor a tömbünk végére érünk már nem érvénes, hogy num1 < num2, mert a 2-est és a 0-t összehasonlítva a 2-es nyer, ezért ezt külön kezeljük
def winner(num1, num2):
    if num1 == num2:
        return 0
    elif num1 == 2 and num2 == 0:
        return 2
    elif num1 < num2:
        return 2
    else:
        return 1

eredmenyek = ['Döntetlen', 'Vesztettél', 'Nyertél']
eredmeny = winner(ellenfel_num, user_num)

print(eredmenyek[eredmeny]+1)