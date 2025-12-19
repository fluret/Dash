import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

raw_data.dropna(axis=0, inplace=True)

for index, col in raw_data.iterrows():
    try:
        float(col.iloc[2])  # 'temp' column is index 2
    except:
        raw_data.drop(index, axis=0, inplace=True)

print(raw_data.head())