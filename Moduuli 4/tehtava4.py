import random

luku = random.randint(1,10)
arvaus = int(input("Arvaa numero: "))
if arvaus == luku:
    print("Oikein")
while arvaus != luku:
    if luku > arvaus:
        print("Liian pieni luku")
    if luku < arvaus:
        print("Liian suuri luku")
    arvaus = int(input("Arvaa uudestaan "))
    if arvaus == luku:
        print("Oikein")




