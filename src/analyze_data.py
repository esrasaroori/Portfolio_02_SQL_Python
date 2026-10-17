import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/processed/diabetic_cleaned.csv")

# Count readmission categories
readmission_counts = df["readmitted"].value_counts()

print("Readmission counts:")
print(readmission_counts)

# Calculate readmission within 30 days
readmitted_within_30_days = (
    df["readmitted"] == "<30"
).sum()

total_visits = len(df)

readmission_rate = (
    readmitted_within_30_days / total_visits
) * 100

print("\nReadmission within 30 days:")
print(f"Visits: {readmitted_within_30_days}")
print(f"Total visits: {total_visits}")
print(f"Rate: {readmission_rate:.2f}%")

# Analyze readmission within 30 days by age group
df["readmitted_within_30_days"] = (
    df["readmitted"] == "<30"
)

age_readmission = (
    df.groupby("age")["readmitted_within_30_days"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)

print("\nReadmission within 30 days by age group (%):")
print(age_readmission)

# Analyze readmission by length of hospital stay
df["readmitted_within_30_days"] = (
    df["readmitted"] == "<30"
)

stay_readmission = (
    df.groupby("time_in_hospital")[
        "readmitted_within_30_days"
    ]
    .mean()
    .mul(100)
    .round(2)
)

print("\nReadmission within 30 days by hospital stay (%):")
print(stay_readmission)

import matplotlib.pyplot as plt

# Plot readmission rate by hospital stay
stay_readmission.plot(kind="bar")

plt.title("30-Day Readmission Rate by Hospital Stay")
plt.xlabel("Length of Hospital Stay (Days)")
plt.ylabel("Readmission Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/readmission_by_stay.png", dpi=300)
plt.show()

