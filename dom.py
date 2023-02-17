from roman import *

t = [str(x) for x in input("vedite rimskoe chislo")]

for i in t:
    print(i, '->' ,roman_to_int(i))

a= [int(x) for x in input("vedite  chislo")]

for i in a:
    print(i, '->',int_to_roman(i))
