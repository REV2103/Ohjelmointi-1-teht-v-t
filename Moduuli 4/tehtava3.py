luvut = int(input("Anna lukuja. Kun olet laittanut tarpeeksi lukuja jätä kenttä tyhjäksi "))
luvut_list = []
while luvut != SyntaxError:
    try:
        luvut = (int(input("Anna lisää lukuja tai jätä kenttä tyhjäksi järjestääksesi luvut ")))
        luvut_list.append(luvut)
    except ValueError:
        luvut_list.sort()
        print(f"Luvut järjestyksessä: {luvut_list}")
        break




