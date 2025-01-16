leiviskat_str = input("Anna leiviskät ")
naulat_str = input("Anna naulat ")
luodit_str = input("Anna luodit ")
leiviskat = float(leiviskat_str)
naulat = float(naulat_str)
luodit = float(luodit_str)
luo_g = luodit*13.3
n_g = naulat*32*13.3
lei_g = leiviskat*20*32*13.3
summa_grammoina = luo_g+n_g+lei_g
sumkg = summa_grammoina//1000
print(f"Summa nykymittojen mukaan: {sumkg:12.0f} kilogrammaa {summa_grammoina%1000:12.2f} grammaa")


