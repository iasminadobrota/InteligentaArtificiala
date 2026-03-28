#Sortati urmatoarea lista dupa a 2-a valoare din fiecare tuplu
# folosind expresii Lambda:

#ex: a = [(0, 2), (4, 3), (9, 9), (10, -1)]
     # sorted_a = [(10, -1), (0, 2), (4, 3), (9, 9)]

a = [(0, 2), (9, 1), (5, 9), (10, -1)]

sorted_a=sorted(a, key=lambda x: x[0])

sorted_b = sorted(a, key=lambda x: x[1])

print("Sortate crescator dupa prima valoare din tuplu:",sorted_a)
print("Sortate crescator dupa a doua valoare din tuplu:", sorted_b)

#am facut si pt prima valoare si am mai schimbat putin valorile ca sa vad diferenta