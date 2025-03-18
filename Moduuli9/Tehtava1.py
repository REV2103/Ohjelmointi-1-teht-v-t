class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, th_nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.th_nopeus = th_nopeus
        self.matka = matka
auto = Auto("ABC-123", "142 km/h", "0 km/h", "0 km")
print(f"Auton rekisteritunnus on {auto.rekisteritunnus} ja sen huippunopeus on {auto.huippunopeus}")