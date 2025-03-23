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

class sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, th_nopeus, matka, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, th_nopeus, matka)
    def kulje(self, aika):
        super().kulje(aika)
        return self.matka


class polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, th_nopeus, matka, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus, th_nopeus, matka)
    def kulje(self, aika):
        super().kulje(aika)
        return self.matka

ei_tesla = sähköauto("ABC-15",180, 100, 0, 52.5)
ei_ford = polttomoottoriauto("ACD-123", 165, 75, 0, 32.3)

ei_ford.kulje(3)
ei_tesla.kulje(3)
print(f" Polttomoottoriauto kulki {ei_ford.matka} kilometriä")
print(f" Sähköauto kulki {ei_tesla.matka} kilometriä")
