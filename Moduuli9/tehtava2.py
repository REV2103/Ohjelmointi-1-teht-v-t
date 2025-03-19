class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, th_nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.th_nopeus = th_nopeus
        self.matka = matka
    def kiihdytä(self, kiihdytys):
        self.th_nopeus = self.th_nopeus+kiihdytys
        if self.th_nopeus > self.huippunopeus:
            self.th_nopeus = self.huippunopeus
        return kiihdytys


auto = Auto("ABC-123", 142, 0 , 0)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} sen huippunopeus on {auto.huippunopeus} km/h ja tämänhetkinen nopeus {auto.th_nopeus} km/h")