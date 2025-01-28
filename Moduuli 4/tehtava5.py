kayttis = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
if kayttis == "python" and salasana == "rules":
    print("Tervetuloa")
yritykset = 0
while yritykset <= 5:
    if kayttis != "python" or salasana != "rules":
        print("Tiedot väärin, ole hyvä ja syötä tiedot uudelleen")
        yritykset = yritykset + 1
        if yritykset == 5:
            print("Pääsy evätty")
            break
        kayttis = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")
        if kayttis == "python" and salasana == "rules":
            print("Tervetuloa")





