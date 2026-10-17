import pandas as pd

# load the raw dataset
df = pd.read_csv("data/raw/diabetes_raw.csv",
 low_memory=False,
 keep_default_na=True)

# confirm that the dataset is downloaded correctly
print("Dataset loaded successfully!")

print("\noriginal dataset shape:")
print(df.shape)

print("\n missing values befor cleaning:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\n duplicated raws:")
print(df.duplicated().sum())

# Remove columns with no variations
Columns_to_remove = ["examide", "citoglipton","weight"]

df= df.drop(columns=Columns_to_remove)

print("\nColumns removed:")
print(Columns_to_remove)

print("\nDataset shape after cleaning:")
print(df.shape)

print("\nRemaining columns:")
print(len(df.columns))


print("\nData types after removing constant columns:")
print(df.dtypes.value_counts())

print("\nColumns with object or string data types:")
print(df.select_dtypes(include=["object", "str"]).columns.tolist())

print("\nMissing values after removing constant columns:")
missing_values = df.isnull().sum()

print(missing_values[missing_values > 0].sort_values(ascending=False))

print("\nTotal missing values:")
print(missing_values.sum())

print("\nDataset shape:")
print(df.shape)


key_columns = [
    "gender",
    "age",
    "time_in_hospital",
    "number_inpatient",
    "number_emergency",
    "number_outpatient",
    "num_medications",
    "diabetesMed",
    "change",
    "readmitted"
]

print("\nMissing values in key analysis columns:")
print(df[key_columns].isnull().sum())

print("\nUnique readmission values:")
print(df["readmitted"].value_counts(dropna=False))



categorical_columns = [
    "gender",
    "age",
    "diabetesMed",
    "change",
    "readmitted"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False))

# save the cleaned dataset to a new csv file

df.to_csv("data/processed/diabetic_cleaned.csv", index=False)

print("\ncleaned dataset saved successfully")
print("\ncleaned dataset shape:", df.shape) 

# Verify the saved dataset
df_check = pd.read_csv("data/processed/diabetic_cleaned.csv")

print("\nVerification of saved dataset:")
print("Saved dataset shape:", df_check.shape)
print("File loaded successfully!")

# Check missing values in the cleaned dataset
missing_values = df_check.isnull().sum()

print("\nColumns with missing values:")
print(
    missing_values[missing_values > 0]
    .sort_values(ascending=False)
)

# Calculate missing value percentages
missing_percentage = (
    df_check.isnull().mean() * 100
)

print("\nMissing value percentages:")
print(
    missing_percentage[missing_percentage > 0]
    .sort_values(ascending=False)
    .round(2)
)

print("Question marks in key columns:")

for column in ["race", "payer_code", "medical_specialty"]:
    print(column, (df[column] == "?").sum())

# Check missing values in diagnosis columns
diagnosis_columns = ["diag_1", "diag_2", "diag_3"]

print("\nMissing diagnosis values:")
print(df[diagnosis_columns].isnull().sum())

# Check missing values in key analysis columns
key_columns = [
    "gender",
    "age",
    "time_in_hospital",
    "number_inpatient",
    "number_emergency",
    "number_outpatient",
    "num_medications",
    "diabetesMed",
    "change",
    "readmitted"
]

print("\nMissing values in key analysis columns:")
print(df[key_columns].isnull().sum())

# Check duplicate rows in the cleaned dataset
print("\nDuplicate rows in cleaned dataset:")
print(df.duplicated().sum())