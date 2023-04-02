import random; # random python könyvtár beimportálása, hogy annak függvényeit használhassuk

guess = random.randint(1,100) # itt a random könyvtár randint függvényével kérünk egy véletlen számot 1 és 100 között

print("Gondoltam egy számot 1 és 100 között.\nTaláld ki! ") # ezzel csak kiíratjuk az utasítás

# TODO: ez csak a debugolás és a fejlesztéshez iratjuk ki a végleges verzióban törölni kell majd
print("for debug only: " + str(guess)) # str függvény a guess változót, ami szám, átalakítja stringgé és így már tudjuk conactálni a másik stringgel

number = 0 # number változót létrehozzuk és adunk neki egy olyan értéket, ami elvileg nem lehet a guess értéke nehogy a while első iterációjából ki is szálljon
game_running = True # ez egy Boolean változó aminek az értéke csak igaz (1) és hamis (0) Boolean egy matematikus volt, akiről a Boolean algebra is ell lett nevezve, irányítás és vezérlés technikában fontos a mai napig

lives = 9 # ez itt a lehetséges próbálkozások száma
trials = 0 # ez a változó őrzi majd a próbálkozásk számát

# while ciklus addig fut, amíg a megadott feltétel igaz. Pont úgy végzi az ellenőzést, ahogyan az if is.
while game_running:
    print("\n=================") # frameket printelünk ki, minden iteráció egy sortöréssel "\n" (new line) kezdődik
    number = int(input("Szerintem: ")) # bekérjük a usertől az értéket, azaz amit tippel. Az int függvény a stringet egyből number változóvá alakítja nekünk, ha ezt nem tetnnénk meg az első if-beli összehasonlításnál hibát dobna a python
    if number < guess: # ha a number kisebb mint, amit ki kell találni, akkor kapjon a user egy üzenetet
        print("Nem, talált. A szám amire gondoltam nagyobb.")
    if number > guess: # és fordított esetben is
        print("Nem, talált. A szám amire gondoltam kisebb.")
    if number == guess: # ha a számot eltalálta a user akkor írjuk ki hogy talált és állítsuk le a játékot
        print("Talált!")
        game_running = False # a game_running értéke itt lesz hamis, azaz a következő ciklusban már be sem lép a whilenál! A program futása leáll.
    if trials >= lives: # ha a próbálokzások száma elérte a lehetséges legtöbbet akkor:
        print("Sajnálom vesztettél!") # ezt kíiratjuk
        game_running = False # és a játékot leállítjuk
    if game_running == True: # ha a fenti vizsgálatok után még mindig fut a játék, akkor
        if lives - trials < 2: # és ha a lehetséges próbálkozásokból már csak 2-nél kevesebb van
            print("Utlosó lehetőség!") # ezt írhuk ki
        else: # minden más esetben pedig ezt:
            print("Már csak " + str(lives-trials) + " lehetőséged maradt!")
    trials += 1 # minden egyes próbálkozás után a "megtörtént" próbálkozások számát növeljük meg eggyel!

# Jegyzet:
# Python dinamikus nyelv, azaz a változók típusát nem kell meghatároznunk, az az értékük megadásakor történik.
# pl. :
#```
# a = 6 # ez egy szám típusú változó lesz
# b = "Katyvasz!" # ez egy string (húr) mmagyarabbúl karakterlánc, vagy szöveg
# c = True # ez pedig Boolean, azaz igaz / hamis True / False értéket vehet fel!
#```
# Fontos tudni a booleanról, hogy a fenti kis programban az if és a while után is valójában booleanok állnak.
# Az if feladata, hogy csak akkor futtassa a programrészt, ha a feltétel teljesül, azaz a következően megadott feltétel True.
# A while pedig addig futtassa a programrészt, amíg a követő feltétel teljesül.
# Ebben a leckében még azt tanultuk meg, hogy bár a változók típusai dinamikisan változhatnak, ennek ellenére mégsem lehet különböző típusokkal egyes műveleteket elvégezni, azokat bizonyos esetekben át kell alakítani.
# Erre használtuk szöveg és szám concatálásakor a számra az: str(number) és a számok összehasolnításához szükségszerűen a user által bevitt szöveget számmá alakítását, azonnal a bevitel után int(text) lásd a 19. sorban.