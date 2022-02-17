# int number = 5;
number = 5
print(number)

# určenie typu premmenej
print(type(number))

# kontrola typov
print(type(number) == int)
print(type(number) == float)

print(isinstance(number, int))
print(isinstance(number, float))


# int number = 5;
# number = 6;
# number = 'a'; - v C je to chyba
# pretypovanie premennej - uložíme hodnotu iného typu
number = 'a'
print(number)
print(type(number))


# viacnásobná inicializácia premenných
a = 0
b = 0

a, b = 0, 0


# rozdiel medzi zoznamom a množinou
lst = [2, 3, 4, 2, 5, 3]
print(lst)

my_set = set(lst)
print(my_set)

# operator +
print("ab" + "cd")
print(True + True)

# ukážka celočíselného delenia
print(11 // 4)

# ukážka umocňovania
print(3 ** 3)


# viacnásobné porovnávanie
x = 2
# x > 3 && x < 10
print(x > 3 and x < 10)
print(3 < x < 10)
print(3 < 10 < x)

# správny postup pri porovnávaní floatov
a = 3.0
b = 3.00000001
print(a == b)
print(abs(a - b) < 0.001)


# rozdiel medzi == a is
print(None == None)
print(None is None)

import numpy as np

print(np.NaN == np.NaN)
print(np.NaN is np.NaN)


# význam odsadenia
a = 5
if a < 10:
    print("a < 10")
    print("a je mensie ako 10")
else:
    print("a >= 10")
print("a je vacsie alebo rovne ako 10")

# ukážka cyklu while
x = 0
# print("nejaka sprava")
while x < 5:
    # pass - prázdna operácia
    print("nejaka sprava")
    x += 1

# ten istý cyklus pomocou for
for i in range(0, 5):
    print('nejaka sprava 2')

# prechádzanie zoznamom
for element in [4, 2, 3, 1, 9, 5]:
    print(element)
