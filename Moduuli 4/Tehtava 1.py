import random
nopat = int(input("Anna noppien lukumäärä: "))
print("Noppien silmäluvut: ")
for nopat in range (0, (nopat)):
    print(random.randint(1,6))