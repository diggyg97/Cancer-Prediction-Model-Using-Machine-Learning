import pandas as pd

s = pd.read_csv('/Users/digvijayghotane/Downloads/USCS_1999_2015_ASCII/BYAREA.txt',delimiter='|')
a = len(s)
print(a)
for i in range(0,a):
        if s.iloc[i][9]=='Brain and Other Nervous System':
            c = s[i][:]
            break
print(c)