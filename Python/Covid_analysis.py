import pandas as pd

df = pd.read_csv("Data/owid-covid-data.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(20))