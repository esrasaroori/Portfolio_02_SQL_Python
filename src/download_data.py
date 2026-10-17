from ucimlrepo import fetch_ucirepo
import pandas as pd

# Fetch the UCI Diabetes dataset
diabetes = fetch_ucirepo(id=296)

# Get features and target
X = diabetes.data.features
y = diabetes.data.targets

# Combine them into one DataFrame
df = pd.concat([X, y], axis=1)

# Display basic information
print("Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nFirst 5 rows:")
print(df.head())

# Save the raw dataset
df.to_csv("data/raw/diabetes_raw.csv", index=False)

print("\nRaw dataset saved successfully!")

