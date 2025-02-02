nimet = set()
annettu_nimi = input("Anna nimi tai paina enter tulostaeksesi listan nimistä: ")
while annettu_nimi != "":
    if annettu_nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(annettu_nimi)
    annettu_nimi = input("Anna nimi tai paina enter tulostaeksesi listan nimistä: ")
else:
    print(nimet)
