import pandas as pd
filepath = r'../datas/data_02.csv'
col_names = ['country','continent','year','pop']
df2 = pd.read_csv(filepath, sep='|', usecols=col_names)
print(df2.head())