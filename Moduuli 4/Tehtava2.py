tuumat_str = input("Anna tuumat: ")
tuumat = float(tuumat_str)
while tuumat >= 0:
    senttimetrit = tuumat*2.54
    print(f"{tuumat} on {senttimetrit} cm")
    break
else:
    print("Anna positiivinen luku")