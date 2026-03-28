#Aveti o listă cu prețuri ale produselor,
# dar unele sunt None (lipsă).
# Folositi filter()  pentru a elimina elementele
# None și map() pentru a aplica o reducere de 10%.

lista_preturi=[20, 55, None, 100, None]

preturi_valide=list(filter(lambda x:x is not None, lista_preturi))

reducere=0.1
preturi_reduse=list(map(lambda x:x*(1-reducere), preturi_valide))

print("Preturi initiale:", lista_preturi)
print("Preturi valide:", preturi_valide)
print("Preturi reduse:", preturi_reduse)
