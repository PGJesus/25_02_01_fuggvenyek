"""3.2 Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)"""

def harommal_oszthatok():
    szamok = []
    while True:
        szam = int(input("Adj meg egy szamot: "))
        if szam < 0:
            break
        szamok.append(szam)
    for szam in szamok:
        if szam % 3 != 0:
            return False
    return True

print(harommal_oszthatok(szamok))