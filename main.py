from random import randint

def vypis_staty_hraca():
    print(f"Hrac {meno} ma hp: {hpHraca} a jeho utok je {utokHraca}.")

def vytvor_nepriatela():
    hp = randint(10,20)
    utok = randint(2,5)
    return hp, utok

def vypis_staty_nepriatela():
    print(f"Nepriatel cislo {nepriatelCislo} ma hp: {hpNepriatela} a jeho utok je {utokNepriatela}.")

meno = input("Zadaj meno: ")

if meno[0] in "qwertyuiopasdfghjklzxcvbnm":
    print("Si normalny ? Prve pismenko mena je od kedy male ?!")
    meno = meno[0].upper() + meno[1:]
    print(f"Tvoje meno od teraz je: {meno}")

##print("Ahoj", meno, "vitaj v hre")
print(f"Ahoj {meno} vitaj v hre")


hpHraca = randint(50,100)
utokHraca = randint(5,15)

hpNepriatela, utokNepriatela = vytvor_nepriatela()
nepriatelCislo = 1

vypis_staty_hraca()
vypis_staty_nepriatela()

while hpHraca > 0:
    if hpNepriatela <= 0:
        nepriatelCislo += 1
        hpNepriatela, utokNepriatela = vytvor_nepriatela()
    print(f"Hrac {meno} utoci")
    hpNepriatela -= utokHraca
    if hpNepriatela <= 0:
        print(f"Nepriatel cislo {nepriatelCislo} zomrel")
        continue
    print(f"Nepriatel cislo {nepriatelCislo} utoci")
    hpHraca -= utokNepriatela
    vypis_staty_hraca()
    print()

print(f"Prehral si. Porazil si {nepriatelCislo} nepriatelov")
