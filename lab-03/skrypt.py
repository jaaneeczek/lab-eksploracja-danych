import pandas as pd

df = pd.read_csv("lab-03/dane.csv")
print("Liczba wierszy:", len(df))
print("Kolumny:", list(df.columns))
print("Braki w kolumnach:")
print(df.isnull().sum())