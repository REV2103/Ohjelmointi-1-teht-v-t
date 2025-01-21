luvut_str = input("Anna lukuja. Kun olet laittanut tarpeeksi lukuja jätä kenttä tyhjäksi tämän promptin jälkeen" )
while luvut_str != "":
    luvut = float(luvut_str)
    luvut_str: input("Anna lisää lukuja: ")
    if luvut_str == "":
        print("OK")
else:
    print("OK")

