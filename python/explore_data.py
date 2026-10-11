import pandas as pd

df = pd.read_excel("data/raw/online_retail_II.xlsx")

print("First 5 rows:")
print(df.head())

print("Dataset shape:")
print(df.shape)

print("Column names:")
print(df.columns)

print("Missing values per column:")
print(df.isnull().sum())

print("Data types:")
print(df.dtypes)

print("Duplicate rows:")
print(df.duplicated().sum())



print("Quantity summary:")
print(df["Quantity"].describe())

print("Price summary:")
print(df["Price"].describe())

print("Unique countries:")
print(df["Country"].nunique())

print("Unique customers:")
print(df["Customer ID"].nunique())

print("Unique products:")
print(df["StockCode"].nunique())


print("Negative quantities:")
print((df["Quantity"] < 0).sum())

print("Negative prices:")
print((df["Price"] < 0).sum())

print("Zero prices:")
print((df["Price"] ==0).sum())



print("Rows with negative prices:")
print(df[df["Price"] < 0])

print("Sample negative quantity transactions:")
print(df[df["Quantity"] < 0].head(20))

print("Sample zero-price transactions:")
print(df[df["Price"]==0].head(20))

