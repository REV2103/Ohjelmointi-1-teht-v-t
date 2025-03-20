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
class kilpailu:
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autot = autot
        self.autolista = []
        for i in range(autot):
            self.autolista.append(Auto(f"ABC-{1 + i}", random.randint(100, 200), 0, 0))
        self.ohi = False

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
        self.kilpailu_ohi()

    def tulosta_tilanne(self):
        taulukon_tunnisteet = ["Rekisteritunnus", "Huippunopeus", "Tämänhetkinen Nopeus", "Kuljettu Matka"]
        print(taulukon_tunnisteet)
        for auto in self.autolista:
            print(f"{auto.rekisteritunnus}, {auto.huippunopeus} km/h, {auto.th_nopeus} km/h, {auto.matka} km")

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matka >= self.kilometrit:
                self.ohi = True
                break

Suuri_Romuralli = kilpailu("Suuri Romuralli", 8000, 10)
while not Suuri_Romuralli.ohi:
    for i in range(10):
        Suuri_Romuralli.tunti_kuluu()
        if Suuri_Romuralli.kilpailu_ohi:
            break
    Suuri_Romuralli.tulosta_tilanne()
Suuri_Romuralli.tulosta_tilanne()
