#Scrieti  o funcție genereaza_factura() care acceptă
# numele clientului, și un număr variabil de produse
# și prețuri folosind **kwargs.


def genereaza_factura(nume_client, **produse):
    print("Factura pentru:", nume_client)

    total = 0

    for produs in produse:
        pret = produse[produs]
        print(produs, "-", pret, "RON")
        total = total + pret

    print("Total:", total, "RON")


genereaza_factura(  "Iasmina", paine=5, lapte=7, oua=10)