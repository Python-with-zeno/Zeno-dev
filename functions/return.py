

def osszed(a, b):
    return a + b
  
def kivon(a, b):
    return a - b
  
def szoroz(a, b):
    return a * b
  
def oszt(a, b):    
    return a / b  

szam1 = 2
szam2 = 3

# eredmeny1 = osszed(szam1, szam2)
# print(eredmeny1)

# print(osszed(5, 8))
# print(kivon(5, 8))
# print(szoroz(5, 8))
# print(oszt(5, 8))

# itt pedig függvénybe fügvényeket helyeztünk el
def bonyolult_matek(szam1, szam2):
  eredmeny1 = osszed(szam1, szam2)
  eredmeny2 = kivon(eredmeny1, szam2)
  eredmény3 = szoroz(eredmeny2, szam1)
  eredmény4 = oszt(eredmény3, szam2)
  return eredmény4

bonyolult_eredmeny = bonyolult_matek(5, 8)
print(bonyolult_eredmeny)