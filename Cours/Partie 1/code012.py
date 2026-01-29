import pandas as pd
filepath = r'../datas/data_01.xlsx'
df1 = pd.read_excel(filepath, sheet_name='Sheet1')
print(df1)