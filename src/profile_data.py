import pandas as pd

df = pd.read_csv("data/raw/diabetes_raw.csv")

print("Dataset shape:")
print(df.shape)

print("\ncolumn information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False))


missing_percent = (df.isnull().sum() / len(df)) * 100

print("\nMissing Values Percentage:")
print(missing_percent.sort_values(ascending=False))

print("\ngender distribution:")
print(df["gender"].value_counts())

print("\nAge distribution:")
print(df["age"].value_counts().sort_index())

print("\nReadmission Distribution:")
print(df["readmitted"].value_counts())

print("\nUnique values in key categorical variables:")

print("\nGender:")
print(df["gender"].unique())

print("\nReadmitted:")
print(df["readmitted"].unique())

print("\nDiabetes medication:")
print(df["diabetesMed"].unique())

print("\nMedication change:")
print(df["change"].unique())

print(df["A1Cresult"].value_counts(dropna=False))
print("\nMax Glucose Serum:")
print(df["max_glu_serum"].value_counts(dropna=False))

print("\nRace:")
print(df["race"].value_counts(dropna=False))

print("\nWeight:")
print(df["weight"].value_counts(dropna=False).head(10))

print("\nPayer Code:")
print(df["payer_code"].value_counts(dropna=False).head(10))

print("\nMedical Specialty:")
print(df["medical_specialty"].value_counts(dropna=False).head(10))

print("\nDiabetes Medication:")
print(df["diabetesMed"].value_counts(dropna=False))

print("\nMedication Change:")
print(df["change"].value_counts(dropna=False))

print("\nReadmission:")
print(df["readmitted"].value_counts(dropna=False))

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Values:")
print("Gender:", df["gender"].nunique())
print("Race:", df["race"].nunique())
print("Age:", df["age"].nunique())
print("Readmitted:", df["readmitted"].nunique())

print(df.columns.tolist())

medication_columns = [
    "metformin",
    "repaglinide",
    "nateglinide",
    "chlorpropamide",
    "glimepiride",
    "acetohexamide",
    "glipizide",
    "glyburide",
    "tolbutamide",
    "pioglitazone",
    "rosiglitazone",
    "acarbose",
    "miglitol",
    "troglitazone",
    "tolazamide",
    "examide",
    "citoglipton",
    "insulin",
    "glyburide-metformin",
    "glipizide-metformin",
    "glimepiride-pioglitazone",
    "metformin-rosiglitazone",
    "metformin-pioglitazone"
]

print("\nMedication Value Counts:")

for column in medication_columns:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False))


print("\nPatient ID column:")
print("patient_nbr" in df.columns)

print("\nAdmission Type:")
print(df["admission_type_id"].value_counts().sort_index())

print("\nDischarge Disposition:")
print(df["discharge_disposition_id"].value_counts().sort_index())

print("\nAdmission Source:")
print(df["admission_source_id"].value_counts().sort_index())

print("\nTime in Hospital:")
print(df["time_in_hospital"].value_counts().sort_index())

print("\nNumber of Lab Procedures:")
print(df["num_lab_procedures"].describe())

print("\nNumber of Procedures:")
print(df["num_procedures"].describe())

print("\nNumber of Medications:")
print(df["num_medications"].describe())

print("\nNumber of Diagnoses:")
print(df["number_diagnoses"].describe())

print("\nOutpatient Visits:")
print(df["number_outpatient"].describe())

print("\nEmergency Visits:")
print(df["number_emergency"].describe())

print("\nInpatient Visits:")
print(df["number_inpatient"].describe())