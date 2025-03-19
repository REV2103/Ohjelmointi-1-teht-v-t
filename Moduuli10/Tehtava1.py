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
h = hissi(1, 5, 1)
h.siirry_kerrokseen(3)
print(h.kerros)
h.siirry_kerrokseen(h.alin)
print(h.kerros)