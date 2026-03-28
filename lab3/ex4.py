#Creati o expresie lambda care va afisa o lista data
# ca input ridicata la patrat.
# ex: my_list = [1, 2, 3] => [1, 4, 9]

my_list = [1, 2, 3]
expresie = list(map(lambda x: x * x, my_list))

print("Expresie lambda:", expresie)