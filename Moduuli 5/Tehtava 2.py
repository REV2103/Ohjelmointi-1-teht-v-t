luvut = input("Anna lukuja. Paina Enter kun olet laittanut niitä tarpeeksi: ")
luvut_list = []
while luvut != "":
    luvut_list.append(int(luvut))
    luvut = input("Anna lisää lukuja tai paina enter kun et halua laittaa enempää ")
else:
    luvut_list.sort(reverse=True)
    print(luvut_list[0:4])
