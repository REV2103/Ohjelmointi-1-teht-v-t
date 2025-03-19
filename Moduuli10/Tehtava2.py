class hissi:
    def __init__(self, alin, ylin, kerros):
        self.alin = alin
        self.ylin = ylin
        self.kerros = kerros
    def kerros_ylös(self):
        self.kerros = self.kerros + 1
    def kerros_alas(self):
        self.kerros = self.kerros - 1
    def siirry_kerrokseen(self, h_kerros):
        if h_kerros < self.kerros:
            for i in range(self.kerros-h_kerros):
                self.kerros_alas()
        elif h_kerros > self.kerros:
            for i in range(h_kerros-self.kerros):
                self.kerros_ylös()

class talo:
    def __init__(self, alin, ylin, hissi_lm):
        self.alin = alin
        self.ylin = ylin
        self.hissi_lm = hissi_lm
        self.hissit = []
        for i in range(hissi_lm):
            self.hissit.append(hissi(self.alin, self.ylin, self.alin))
    def aja_hissiä(self, hissi_num, kohdker):
        hal_hissi = self.hissit[hissi_num-1]
        while kohdker > self.ylin:
            kohdker-1
        while kohdker < self.alin:
            kohdker+1
        else:
           hal_hissi.siirry_kerrokseen(kohdker)
           print(hal_hissi, hal_hissi.kerros)
Majakka = talo(1, 4, 3)
Majakka.aja_hissiä(2, 2)




