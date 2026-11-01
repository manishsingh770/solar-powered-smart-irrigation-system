
import json

file_path = "Dataset on irrigation for Tomato/tomato_water_sensor_data.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Data type:", type(data).__name__)

if isinstance(data, dict):
    print("\nAvailable keys:")
    print(list(data.keys()))

elif isinstance(data, list):
    print("\nNumber of records:", len(data))
    if data:
        print("\nFirst record:")
        print(data[0])

print("\nSample data:")
print(str(data)[:3000])
