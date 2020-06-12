import pandas as pd
my_serials = pd.Series([5,6,7,8,9], index =['a','b', 'c', 'd', 'e'])
print(my_serials['a':'c']) #этот вариант у нас называется слайсом
print(my_serials.index)
print(my_serials.values)
my_serials['a':'c'] = 0
print(my_serials)


#логические условия
mys_serials3 = my_serials[my_serials > 5] * 2
print(mys_serials3)