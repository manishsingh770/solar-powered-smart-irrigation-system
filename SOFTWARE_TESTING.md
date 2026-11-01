
# Software Testing Report

## Project
Solar-Powered Smart Irrigation System

## Testing Environment
- Programming language: Python
- Dashboard framework: Streamlit
- Data processing: Pandas
- Visualization: Matplotlib
- Datasets:
  - Original irrigation dataset: 55 readings
  - Tomato JSON dataset: 393 records

## Dataset Quality
- Total rows: 55
- Total columns: 4
- Missing values: 0
- Duplicate rows: 0

## Tomato JSON Dataset Analysis
- Total JSON records: 393
- Required attributes checked: 6
- Missing values in required attributes: 0
- Soil moisture attribute: moisturePercentage
- Project irrigation threshold: 40%

## Soil Moisture Analysis
- Minimum moisture: 22%
- Maximum moisture: 72%
- Average moisture: 45.35%

## Irrigation Logic Testing

- Total boundary test cases: 7
- Passed: 7
- Failed: 0
- Test result: PASS

## Tomato JSON Irrigation Testing

- Total records: 393
- Project threshold: 40%
- Pump ON: 6
- Pump OFF: 387
- Pump ON percentage: 1.53%
- Test result: PASS

## Visualization Testing

- Soil moisture monitoring graph: Generated
- 40% threshold line: Displayed
- Pump ON/OFF decision graph: Generated
- Graph export: Successful

## Limitations

- The datasets contain simulated or recorded data, not
  measurements from our implemented hardware.
- Physical pump operation has not been tested.
- Solar power generation and battery backup have not
  been physically tested.
- Blynk IoT integration is planned for future development.
