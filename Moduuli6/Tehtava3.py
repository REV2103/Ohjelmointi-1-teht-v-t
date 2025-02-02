def litrat(galloonat):
    G = galloonat*3.785
    return G
Annetut_galloonat = (int(input("Anna galloonat: ")))
while Annetut_galloonat > 0:
    tulos = litrat(Annetut_galloonat)
    print(f"{Annetut_galloonat} galloonaa on {tulos} litraa ")
    Annetut_galloonat = (int(input("Anna galloonat: ")))
else:
    print("Negatiivinen Galloonamäärä annettu, ohjelma lopettaa toimintansa.")


