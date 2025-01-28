lukulista = [*range(2, 1000)]
luku = (int(input("Anna luku: ")))
laskulista = []
for n in lukulista:
    if luku != n:
        lasku = (luku%n)
        laskulista.append(lasku)
if 0 not in laskulista or luku == 1:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")

