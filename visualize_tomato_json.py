
import json
import pandas as pd
import matplotlib.pyplot as plt

file_path = (
    "Dataset on irrigation for Tomato/"
    "tomato_water_sensor_data.json"
)

with open(file_path, "r", encoding="utf-8") as file:
    records = json.load(file)

df = pd.DataFrame(records)

THRESHOLD = 40

df["simulated_pump_status"] = (
    df["moisturePercentage"] < THRESHOLD
)

# Plot soil moisture
plt.figure(figsize=(12, 5))

plt.plot(
    df.index,
    df["moisturePercentage"],
    label="Soil Moisture (%)"
)

plt.axhline(
    y=40,
    linestyle="--",
    label="Minimum Moisture Threshold (40%)"
)

plt.xlabel("Record Number")
plt.ylabel("Soil Moisture (%)")
plt.title("Tomato Soil Moisture and Irrigation Threshold")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/tomato_moisture_graph.png",
    dpi=150
)

plt.show()

print("Graph saved to results/tomato_moisture_graph.png")

# Plot simulated pump ON/OFF decisions
plt.figure(figsize=(12, 4))

plt.step(
    df.index,
    df["simulated_pump_status"].astype(int),
    where="post"
)

plt.yticks([0, 1], ["Pump OFF", "Pump ON"])
plt.xlabel("Record Number")
plt.ylabel("Simulated Pump Status")
plt.title("Tomato Irrigation Decisions (40% Threshold)")
plt.grid(True, axis="x", alpha=0.3)
plt.tight_layout()

plt.savefig(
    "results/tomato_pump_decisions.png",
    dpi=150
)

plt.show()

print("\nPump status summary:")
print(
    df["simulated_pump_status"]
    .value_counts()
    .rename(index={True: "Pump ON", False: "Pump OFF"})
)

print("\n--- Irrigation Test Summary ---")
print("Total records:", len(df))
print("Pump ON:", (df["moisturePercentage"] < 40).sum())
print("Pump OFF:", (df["moisturePercentage"] >= 40).sum())

print(
    "Pump ON percentage:",
    round((df["moisturePercentage"] < 40).mean() * 100, 2),
    "%"
)


