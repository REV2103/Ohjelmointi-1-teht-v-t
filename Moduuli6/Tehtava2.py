import random

def noppa(Tahkot):
    sl = random.randint(1, Tahkot)
    return sl
Tahkojen_maara = float(input("Anna tahkojen määrä: "))
tulos = (noppa(Tahkojen_maara))
while tulos != Tahkojen_maara:
    print(f"Nopan silmäluku: {tulos}")
    tulos = (noppa(Tahkojen_maara))
    print("Heitetään noppaa uudelleen")
else:
    print("Sait nopan suurimman silmäluvun. Hyvä sinä! :D")
