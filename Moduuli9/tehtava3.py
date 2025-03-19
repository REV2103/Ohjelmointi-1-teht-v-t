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
    def kulje(self, aika):
        self.matka = aika*self.th_nopeus
        return aika


auto = Auto("ABC-123", 142, 0 , 2000)
auto.kiihdytä(60)
auto.kulje(1.5)
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} sen huippunopeus on {auto.huippunopeus} km/h, tämänhetkinen nopeus {auto.th_nopeus} km/h ja kuljettu matka on {auto.matka} km")