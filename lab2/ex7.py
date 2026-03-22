comentariu = input("Introdu un comentariu: ")

pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
negative = ["urat", "prost", "groaznic", "dezamagitor"]

gasit_pozitiv = False
gasit_negativ = False

for cuvant in pozitive:
    if cuvant in comentariu:
        gasit_pozitiv = True

for cuvant in negative:
    if cuvant in comentariu:
        gasit_negativ = True

if gasit_pozitiv:
    print("Comentariu pozitiv!")
elif gasit_negativ:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")