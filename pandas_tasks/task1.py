import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

types = [mylist, myarr, mydict]

series = []
for i in types:
    series.append(pd.Series(i))

for i in series:
    print(i)