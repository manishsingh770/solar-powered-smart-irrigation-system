
import pandas as pd

# Load the cleaned dataset
data = pd.read_csv("cleaned_irrigation_data.csv")

# Basic dataset information
print("===== DATASET OVERVIEW =====")
print("Total rows:", len(data))
print("Total columns:", len(data.columns))
print("Column names:", data.columns.tolist())

# Missing values and duplicates
print("\n===== DATA QUALITY =====")
print("\nMissing values:")
print(data.isnull().sum())
print("\nDuplicate rows:", data.duplicated().sum())

# Soil moisture statistics
print("\n===== SOIL MOISTURE ANALYSIS =====")
print(data["soil_moisture"].describe().round(2))

print("\nMinimum moisture:",
      data["soil_moisture"].min(), "%")
print("Maximum moisture:",
      data["soil_moisture"].max(), "%")
print("Average moisture:",
      round(data["soil_moisture"].mean(), 2), "%")

# Irrigation decisions at the 40% threshold
threshold = 40

data["pump_status"] = data["soil_moisture"].apply(
    lambda x: "ON" if x < threshold else "OFF"
)

print("\n===== SIMULATED IRRIGATION ANALYSIS =====")
print(data["pump_status"].value_counts())

pump_on = (data["pump_status"] == "ON").sum()
pump_off = (data["pump_status"] == "OFF").sum()

print("Readings below threshold:", pump_on)
print("Readings at/above threshold:", pump_off)
print("Percentage below threshold:",
      round(pump_on / len(data) * 100, 2), "%")

# Solar availability counts
print("\n===== SOLAR AVAILABILITY =====")
print(data["solar_available"].value_counts())

# Save the analysis results
data.to_csv("analyzed_irrigation_data.csv", index=False)

print("\nSaved analyzed data to analyzed_irrigation_data.csv")
