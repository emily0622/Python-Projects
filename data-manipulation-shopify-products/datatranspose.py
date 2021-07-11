import pandas as pd
import json

df = pd.read_csv(r"C:\\Users\\User\\Desktop\\Python-Projects\\Fetching-Stores.csv", encoding= 'unicode_escape')
print(df)

# DataFrameName.insert(loc, column, value, allow_duplicates = False)