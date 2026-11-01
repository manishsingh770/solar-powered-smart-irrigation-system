
import json
import pandas as pd

file_path = (
    "Dataset on irrigation for Tomato/"
    "tomato_water_sensor_data.json"
)

with open(file_path, "r", encoding="utf-8") as file:
    records = json.load(file)

df = pd.DataFrame(records)

# Check required attributes
required = [
    "temperature",
    "humidity",
    "moisturePercentage",
    "minTomatoMoisture",
    "maxTomatoMoisture",
    "motorValue",
]

print("Dataset shape:", df.shape)
print("\nAvailable columns:")
print(df.columns.tolist())

print("\nRequired columns present:")
for col in required:
    print(f"{col}: {col in df.columns}")

# Analyze moisture readings
print("\nMoisture percentage statistics:")
print(df["moisturePercentage"].describe())

print("\nExisting threshold values:")
print(df["minTomatoMoisture"].value_counts().head())

print("\nMissing values in key columns:")
print(df[required].isnull().sum())

# Apply our project's 40% threshold
THRESHOLD = 40

df["simulated_pump_status"] = (
    df["moisturePercentage"] < THRESHOLD
).map({True: "ON", False: "OFF"})
df["projectThreshold"] = THRESHOLD

print("\nSimulated pump status counts:")
print(df["simulated_pump_status"].value_counts())

print("\nSample results:")
print(
    df[
        [
            "moisturePercentage",
            "projectThreshold",
            "simulated_pump_status",
        ]
    ].head(10)
)

df.to_csv(
    "results/tomato_json_logic_test.csv",
    index=False,
)

print("\nResults saved to results/tomato_json_logic_test.csv")
