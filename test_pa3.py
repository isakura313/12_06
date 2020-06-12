import pandas as pd
#некий альтернативный синтаксис

slovar = {'a': 3, 'b':4, 'c':5}
my_serials = pd.Series(slovar)
#так очень удобно работать например с хеш таблицами
print(my_serials)
