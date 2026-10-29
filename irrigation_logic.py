
def irrigation_decision(moisture, threshold=40):
    if moisture < threshold:
        return "ON"
    return "OFF"


# Test the irrigation logic
test_readings = [25, 35, 40, 55, 70]

for moisture in test_readings:
    status = irrigation_decision(moisture)
    print(f"Moisture: {moisture}% -> Pump: {status}")
