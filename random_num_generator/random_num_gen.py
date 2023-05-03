import random # importáljuk a random python libraryt - hogy ezzel tudjunk létrehozni majd véletlen számot.

komputer_valasztasa = random.randint(0, 2) # Máris létrehozunk egy változót, aminek sorsolhatunk egy véletlen számot 0 és 2 között, tehát 0, 1, 2 lehet.

"""
A tömb egy komplex változó, amibe több más változót lehet beletenni, úgy lehet elképzelni, mint egy könyvtárat, vagy egy csomagot, amibe belepakolhatsz.
A tömb indexelése 0-tól kezdődik. Ezekkel az indexekkel lehet elérni az adott lemeket, persz ehhez tudnunk kell, hogy melyik elem hányadik indexen helyezkedik el!
Azért szokták mondani, hogy a programozónak 9 ujja van a 0, az 1, a 2, a 3 ... és a 9! :D
"""
#               0       1       2 - a tömb indexei és a hozzá tartozó értékek
kopapirollo = ["kő", "papír", "olló"] # tömb vagy array változó

# Ide konzolba kiiratunk pár üzenetet, hogy a programunk barátságos legyen!
print('Üdvözöllek a játékban!')
print('Ez egy kő papír olló játék.')

ervenyes_valasztas = True # ezzel a változóval fogjuk szabályozni a "végtelen" ciklusunkból való kiszállást... legalábbis nekem ez volt a tervem, de te egy tök jó megoldást a break-et hoztad be!
valasztasok_szama = 3 # ebben a változóban őrizzük felhasználó választásainak számát! Azaz hány lehetősége van még a feljhasználónak.
felh_valasztasa = 0 # ebben a változóban pedig a elhasználó vaálsztását

# Ez egy while cuiklus, amibe akkor lép bele a python és a benne lépő kódot akkor futtatja, ha a while utáni feltétel igaz, azaz True! láthatod, hogy pár sorral feljebb True értéket adtunk az ervenyes_valasztas változónak, tehát első alkalommal be is fog lépni!
while ervenyes_valasztas:
  if valasztasok_szama < 1: # itt megvizsgáljuk a van e még lehetősége a felhasználónkank újabb próbálkozást tennie arra, hogy értelmes választ adjon...
    print('Túl sok rossz választ adtál meg! Legközelebb figyelj jobban!') # ha már nincs neki több a ptyhon ebbe a scpoeba is belép!
    break # és a fenti sor kiiratása után leállítjuk a while loopunk futtatását!

  felh_valasztasa = int(input('Add meg a választásod: 0 - kő, 1 - papír, 2 - olló: ')) # itt megkérjük a felhasználónkat, hogy válasszon a 0, 1 vagy 2 számok megadásával! Mivel az input mindig string (szöveg) értéket ad nekünk, ezért az int függvénnyel máris számmá alakítjuk, hogy majd tudjuk használni a tömbünk indexe ként.

  valasztasok_szama = valasztasok_szama - 1 # minden egyes iterációban, azaz a while loopunk végrehajtásakor csökkentjük a felhasználónk lehetőségeinek számát.

  if felh_valasztasa < 0 or felh_valasztasa > 2: # ellenőrizzük hogy a felhasználó jó értéket adott e meg, azaz a bevitt szám értéke, ha 0-nál kisebb, !!!vagy!!! 2-nél nagyobb akkor nem megfelelő!
    print('A választásod nem megfelelő!') # a user rosszat választott, erről tájékoztatjuk.
  else:
    print('A te választásod: ' + kopapirollo[felh_valasztasa]) # A tömbből kiválsztjuk a megadott értrknek megfelelő szöveget, index alapján.
    break # megszakítjuk érvényes választás esetén a while loopunkat.


'''
Itt a játékszabálynak megfelelően meghozzuk a döntést, hogy ki győzőtt!
'''
#    kő                       papír
if felh_valasztasa == 0 and komputer_valasztasa == 1:
  print("Komputer győzőtt! Mert a papír üti a követ.")
#    papír                     olló
if felh_valasztasa == 1 and komputer_valasztasa == 2:
  print("Komputer győzőtt! Mert az olló üti a papírt.")
#    olló                     kő
if felh_valasztasa == 2 and komputer_valasztasa == 0:
  print("Komputer győzőtt! Mert a kő üti az ollót.")

#    kő                        papír
if komputer_valasztasa == 0 and felh_valasztasa == 1:
  print("Te győztél! Mert a papír üti a követ.")
#    papír                     olló
if komputer_valasztasa == 1 and felh_valasztasa == 2:
  print("Te győztél! Mert az olló üti a papírt.")
#    olló                      kő
if komputer_valasztasa == 2 and felh_valasztasa == 0:
  print("Te győztél! Mert a kő üti az ollót.")

# ha a felhasználó és a komputer is azonosat választ akkor döntetlen
if felh_valasztasa == komputer_valasztasa:
  print("Döntetlen! Mindkettőtök választása: " + kopapirollo[komputer_valasztasa])
