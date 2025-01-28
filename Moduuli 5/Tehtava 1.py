import random
nopat= int(input("Anna noppien lukumäärä: "))
nop_list = []
for nopat in range (0, (nopat)):
    noppa = int(random.randint(1,6))
    nop_list.append(noppa)
print(f"Noppien silmäluvut: {nop_list}" )
print(f"Silmälukujen summa: {sum(nop_list)}")
