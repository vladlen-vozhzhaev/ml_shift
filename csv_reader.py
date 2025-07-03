import pandas as pd

data_my = {"name": ["Катя", "Аня"], 'age': [33, 42]}
my_df = pd.DataFrame.from_dict(data_my)

data_csv = pd.read_csv('ex.csv', sep=';', header=0)
print(pd.concat([my_df, data_csv], ignore_index=True))