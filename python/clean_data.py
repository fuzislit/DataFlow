import pandas as pd

#Load raw data
df = pd.read_excel("data/raw/online_retail_II.xlsx")

print("Original rows:", len(df))

#  Remove exact duplicate rows
df = df.drop_duplicates()

#Remove accounting adjustment rows with negative prices
df = df[df["Price"] >= 0]

#Remove zero-price transactions
df = df[df["Price"] > 0]

print("Rows after cleaning:", len(df))

df.to_csv("data/processed/online_retail_cleaned.csv", index=False)

print("Cleaned data saved.")