import pandas as pd
from database import create_connection

# Load the cleaned dataset
df = pd.read_csv("data/processed/diabetic_cleaned.csv")

print("Cleaned dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Inspect dataset columns and data types
print("\nDataset columns and data types:")
print(df.dtypes.to_string())

# Create a MySQL connection
connection = create_connection()
cursor = connection.cursor()

# Build SQL column definitions
column_definitions = []

for column, dtype in df.dtypes.items():
    if str(dtype).startswith("int"):
        sql_type = "INT"
    else:
        sql_type = "VARCHAR(255)"

    column_definitions.append(
        f"`{column}` {sql_type} NULL"
    )

columns_sql = ",\n".join(column_definitions)

create_table_query = f"""
CREATE TABLE IF NOT EXISTS diabetes_encounters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    {columns_sql}
)
"""

cursor.execute(create_table_query)
connection.commit()

print("\nTable diabetes_encounters is ready!")

cursor.close()
connection.close()


# Reconnect to MySQL for data import
connection = create_connection()
cursor = connection.cursor()

# Prepare the INSERT statement
data_columns = df.columns.tolist()
columns_sql = ", ".join(f"`{column}`" for column in data_columns)
placeholders = ", ".join(["%s"] * len(data_columns))

insert_query = f"""
INSERT INTO diabetes_encounters ({columns_sql})
VALUES ({placeholders})
"""

# Convert missing values to Python None
df_for_import = df.astype(object).where(pd.notna(df), None)

# Insert data in batches of 1000 rows
batch_size = 1000

for start in range(0, len(df_for_import), batch_size):
    batch = df_for_import.iloc[start:start + batch_size]
    records = list(batch.itertuples(index=False, name=None))

    cursor.executemany(insert_query, records)
    connection.commit()

    print(f"Imported {min(start + batch_size, len(df_for_import))} / {len(df_for_import)} rows")

cursor.close()
connection.close()

print("\nData import completed!")
