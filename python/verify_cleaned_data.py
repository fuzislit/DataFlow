import pandas as pd

df = pd.read_csv("data/processed/online_retail_cleaned.csv")

print("Cleaned dataset shape:")
print(df.shape)

print("Missing values:")
print(df.isnull().sum())

print("Duplicate rows:")
print(df.duplicated().sum())

print("Negative prices:")
print((df["Price"] < 0).sum())

print("Zero prices:")
print((df["Price"] == 0).sum())

print("Negative quantities:")
print((df["Quantity"] < 0).sum())

print("Sample data:")
print(df.head())