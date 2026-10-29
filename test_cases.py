
from irrigation_logic import irrigation_decision

test_cases = [
    (20, "ON"),
    (35, "ON"),
    (40, "OFF"),
    (55, "OFF"),
    (80, "OFF")
]

passed = 0

print("===== IRRIGATION LOGIC TESTING =====")

for moisture, expected in test_cases:
    actual = irrigation_decision(moisture)
    result = "PASS" if actual == expected else "FAIL"

    if result == "PASS":
        passed += 1

    print(
        f"Moisture={moisture}% | "
        f"Expected={expected} | "
        f"Actual={actual} | {result}"
    )

print(f"\nTests passed: {passed}/{len(test_cases)}")
