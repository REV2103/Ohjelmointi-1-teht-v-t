import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, th_nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.th_nopeus = th_nopeus
        self.matka = matka
    def kiihdytä(self, kiihdytys):
        self.th_nopeus = self.th_nopeus+int(kiihdytys)
        if self.th_nopeus > self.huippunopeus:
            self.th_nopeus = self.huippunopeus
        return self.th_nopeus
    def kulje(self, aika):
        self.matka += aika * self.th_nopeus
        return self.matka
autolista = []
taulukon_tunnisteet = ["Rekisteritunnus", "Huippunopeus", "Tämänhetkinen Nopeus", "Kuljettu Matka"]
for i in range(10):
    autolista.append(Auto(f"ABC-{1+i}", random.randint(100, 200), 0, 0))
ktk = False
while not ktk:
    for auto in autolista:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
            if auto.matka >= 10000:
                ktk = True
print(taulukon_tunnisteet)
for auto in autolista:
    print(f"{auto.rekisteritunnus}, {auto.huippunopeus} km/h, {auto.th_nopeus} km/h, {auto.matka} km")



