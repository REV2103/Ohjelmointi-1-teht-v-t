class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"Julkaisun nimi on {self.nimi}")
class kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Sen tyyppi on kirja, kirjoittaja on {self.kirjoittaja} ja sivumäärä {self.sivumäärä}")
class lehti(julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Sen tyyppi on lehti ja päätoimittaja on {self.päätoimittaja}")
julkaisut = []
julkaisut.append(kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(lehti("Aku Ankka", "Aki Hyyppä"))
for i in julkaisut:
    i.tulosta_tiedot()
