hemgl_str = input("Anna hemoglobiiniarvo (g/l): ")
sukupuoli = input("Anna sukupuoli: ")
hemgl = float(hemgl_str)
if sukupuoli == "Nainen" and 117<=hemgl<=175 or sukupuoli == "Mies" and 134<=hemgl<=195:
    print("Hemoglobiiniarvo normaali")
elif sukupuoli == "Nainen" and hemgl < 117 or sukupuoli == "Mies" and hemgl < 134:
    print("Hemoglobiiniarvo alhainen")
elif sukupuoli == "Nainen" and hemgl > 175 or sukupuoli == "Mies" and hemgl > 195:
    print("Hemoglobiiniarvo korkea")
else:
    print("Virheelliset tiedot, ole hyvä ja syötä tiedot uudestaan")