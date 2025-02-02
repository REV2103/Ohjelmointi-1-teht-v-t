import random

def noppa():
    sl = random.randint(1, 6)
    return sl
while noppa() != 6:
    print(f"Silmäluku: {noppa()}")
    print("Heitetään noppaa uudelleen")
    noppa()
else: print("Sait kutosen :D")




