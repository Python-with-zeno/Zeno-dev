import time

# függvényt "def" kulcsszóval lehet létrehozni
# a függvény neve után zárójelben lehet megadni a paramétereket
# a paramétereket vesszővel kell elválasztani
# a függvény visszatérési értékét a "return" kulcsszóval lehet megadni

# a függvény utasításokat lehet belepakolni, ez egy utasítás csomag.

def osszead(a, b):
    print("Összeadás kezdődik!")
    print("Első szám: " + str(a))
    print("Második szám: " + str(b))
    time.sleep(3)
    print("Kérem várjon...")
    time.sleep(3)
    print("Az eredmény: " + str(a + b))
    
# a függvényt meghívni a nevével lehet, zárójelben a paramétereket kell megadni
# osszead(5, 6)

# mi történik, ha nem adunk meg paramétereket?
# osszead()

# a függvény azért jó, mert nem kell mindig ugyanzt a kódot leírnunk
# ha többször is szeretnénk ugyanazt a kódot lefuttatni, akkor elég a függvényt meghívni
# osszead(5, 6)
# osszead(10, 20)
# osszead(100, 200)

# ha egy tömbbe teszzük az adatainkat, ekkor pedig egy ciklussal végigmehetünk rajta, és a függvényt meghívhatjuk a  foron belül
szamok = [[7,6], [11,3], [57,34], [100, 200]]

for szam in szamok:
    osszead(szam[0], szam[1])