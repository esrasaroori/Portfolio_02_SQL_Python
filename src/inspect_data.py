import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/raw/diabetes_raw.csv")

print("Dataset loaded successfully!")

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

