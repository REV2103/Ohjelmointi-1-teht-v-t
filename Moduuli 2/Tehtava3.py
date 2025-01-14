kanta_str = input("Anna suorakulmion kanta metreinä ")
korkeus_str = input("Anna suorakulmion korkeus metreinä ")
kanta = float(kanta_str)
korkeus = float(korkeus_str)
ala = kanta*korkeus
piiri = (kanta*2)+(korkeus*2)
print(f"Suorakulmion pinta-ala neliömetreinä: {ala}")
print(f"Suorakulmion piiri metreinä: {piiri}")