vuosi_str = input("Anna vuosiluku: ")
vuosi = int(vuosi_str)
if (vuosi%4) == 0:
    print("Vuosi on karkausvuosi")
elif (vuosi%4) != 0:
    print("Vuosi ei ole karkausvuosi")
else:
    print ("Ei ole vuosiluku, ole hyvä ja syötä numerot uudelleen.")
