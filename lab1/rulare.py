my_list = [1, 2, '3', True]  # We assume this list won't mutate for each example below

len(my_list)  # 4
my_list.index('3')  # 2
my_list.count(2)  # 1 --> count how many times 2 appears

my_list[3]  # True
my_list[1:]  # [2, '3', True]
my_list[:1]  # [1]
my_list[-1]  # True
my_list[:]  # [1, 2, '3', True]
my_list[::-1]  # [True, '3', 2, 1]
my_list[0:3:2]  # [1, '3']

# : is called slicing and has the format [ start : end : step ]
my_list * 2  # [1, 2, '3', True, 1, 2, '3', True]
my_list + [100]  # [1, 2, '3', True, 100] --> doesn't mutate original list

my_list.append(100)  # None --> Mutates original list
# or
my_list += [100]

my_list.extend([100, 200])  # None --> Mutates original list

my_list.insert(2, '!!!')  # Inserts item at index

' '.join(['Hello', 'There'])  # 'Hello There'
basket = ['apples', 'pears', 'oranges']

new_basket = basket.copy()
new_basket2 = basket[:]

[1, 2, 3].pop()  # 3
[1, 2, 3].pop(1)  # 2
[1, 2, 3].remove(2)  # removes first occurrence
[1, 2, 3].clear()  # []

del [1, 2, 3][0]

[1, 2, 5, 3].sort()  # [1, 2, 3, 5]
[1, 2, 5, 3].sort(reverse=True)  # [5, 3, 2, 1]
[1, 2, 5, 3].reverse()  # [3, 5, 2, 1]

sorted([1, 2, 5, 3])  # [1, 2, 3, 5]
list(reversed([1, 2, 5, 3]))  # [3, 5, 2, 1]

1 in [1, 2, 5, 3]  # True

min([1, 2, 3, 4, 5])  # 1
max([1, 2, 3, 4, 5])  # 5
sum([1, 2, 3, 4, 5])  # 15

mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]

first, *x, last = mList

print(first)  # 63
print(last)   # 10

with open("myfile.txt") as f:
    lines = [line.strip() for line in f]

    my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}

    my_dict['name']  # John Doe
    len(my_dict)  # 3

    list(my_dict.keys())
    list(my_dict.values())
    list(my_dict.items())

    my_dict['favourite_snack'] = 'Grapes'

    my_dict.get('age')  # 25
    my_dict.get('ages', 0)  # default value

    del my_dict['name']
    my_dict.pop('name', None)

    my_tuple = ('apple', 'grapes', 'mango', 'grapes')

    apple, grapes, mango, grapes = my_tuple

    len(my_tuple)  # 4
    my_tuple[2]  # mango
    my_tuple[-1]  # grapes

    # Immutability
    # my_tuple[1] = 'donuts'  # TypeError
    # my_tuple.append('candy')  # AttributeError

    my_tuple.index('grapes')  # 1
    my_tuple.count('grapes')  # 2

    my_set = set()

    my_set.add(1)
    my_set.add(100)
    my_set.add(100)  # no duplicates

    new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]

    set(new_list)  # {1, 2, 3, 4, 5, 6}

    my_set.remove(100)
    my_set.discard(100)
    my_set.clear()

    new_set = {1, 2, 3}.copy()

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    set3 = set1.union(set2)
    set4 = set1.intersection(set2)
    set5 = set1.difference(set2)
    set6 = set1.symmetric_difference(set2)

    set1.issubset(set2)
    set1.issuperset(set2)
    set1.isdisjoint(set2)

    # hashable --> can be used as key in dict

    frozenset([1, 2, 3])

    type(None)  # NoneType

    a = None

