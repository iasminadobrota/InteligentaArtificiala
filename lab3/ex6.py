#Scrieti un program Python pentru a filtra o lista de numere
# intregi folosind expresii Lambda si functia filter().
#ex: orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      #even_list = [2, 4, 6, 8, 10]
      #odd_list = [1, 3, 5, 7, 9]

#-----------
#def even(lista):
 #   return lista % 2 == 0
                            #varianta fara lambda
#def odd(lista):
 #   return lista % 2 != 0



orig_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_even = list(filter(lambda x: x % 2 == 0, orig_list))
                                    #varianta cu lambda
filtered_odd = list(filter(lambda x: x % 2 != 0, orig_list))

#filtered_even = list(filter(even, orig_list))
#filtered_odd = list(filter(odd, orig_list))

print("Numerele pare sunt:",filtered_even)
print("Numerele impare sunt:",filtered_odd)