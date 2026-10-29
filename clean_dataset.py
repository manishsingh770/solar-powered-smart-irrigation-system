
import pandas as pd

# 1. Load the original dataset
data = pd.read_csv("irrigation_data_55.csv")

print("Original dataset shape:", data.shape)

# 2. Remove extra spaces from column names
data.columns = data.columns.str.strip()

# 3. Remove duplicate rows
data = data.drop_duplicates()

# 4. Convert moisture values to numeric
data["soil_moisture"] = pd.to_numeric(
    data["soil_moisture"],
    errors="coerce"
)

# 5. Standardize text columns
for column in ["time", "solar_available", "pump_status"]:
    data[column] = data[column].astype("string").str.strip()

data["solar_available"] = data["solar_available"].str.capitalize()
data["pump_status"] = data["pump_status"].str.upper()

# 6. Remove missing or invalid values
data = data.dropna(
    subset=["time", "soil_moisture", "solar_available"]
)

data = data[
    data["soil_moisture"].between(0, 100)
]

data = data[
    data["solar_available"].isin(["Yes", "No"])
]

# 7. Recalculate pump status using the threshold
threshold = 40

data["pump_status"] = data["soil_moisture"].apply(
    lambda moisture: "ON" if moisture < threshold else "OFF"
)

# 8. Save the cleaned dataset
data.to_csv("cleaned_irrigation_data.csv", index=False)

# 9. Display cleaning summary
print("\nCleaned dataset shape:", data.shape)
print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:", data.duplicated().sum())
print("\nCleaned data preview:")
print(data.head())

print("\nSaved as cleaned_irrigation_data.csv")
