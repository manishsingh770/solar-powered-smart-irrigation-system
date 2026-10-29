# Solar-Powered Smart Irrigation System

## 1. Project Overview

The Solar-Powered Smart Irrigation System is a software-based prototype designed to improve water management in agriculture. It uses soil moisture readings and threshold-based logic to determine when irrigation is required.

The current prototype uses a simulated dataset and an interactive Streamlit dashboard to demonstrate irrigation decisions. The future goal is to integrate the software with physical hardware powered by solar energy.

## 2. Problem Statement

Traditional irrigation methods can lead to unnecessary water consumption, require manual monitoring, and depend on electricity. This project aims to demonstrate an automated irrigation approach that uses soil moisture levels to determine when watering is needed.

## 3. Project Objectives

- Monitor and analyse soil moisture readings.
- Determine pump status using a predefined moisture threshold.
- Visualize irrigation data through an interactive dashboard.
- Clean and analyse the dataset to improve data quality.
- Prepare the software prototype for future hardware integration.

## 4. Technologies Used

- **Programming Language:** Python
- **Dashboard:** Streamlit
- **Data Analysis:** Pandas
- **Data Visualization:** Matplotlib and Streamlit charts
- **Data Storage:** CSV files
- **Version Control:** Git and GitHub

## 5. Project Features

- Simulated dataset containing 55 readings.
- Data cleaning and validation.
- Threshold-based irrigation decision logic.
- Interactive soil moisture threshold slider.
- Summary metrics and soil moisture visualization.
- Pie chart showing readings below and at or above the threshold.
- Tabular display of irrigation data.
- Download option for processed data.
- Automated testing of irrigation decision logic.

## 6. Dataset Description

The simulated dataset contains the following attributes:

| Attribute | Description |
|---|---|
| `time` | Time associated with each reading |
| `soil_moisture` | Soil moisture percentage |
| `solar_available` | Indicates solar availability |
| `pump_status` | Simulated pump status, ON or OFF |

**Note:** The dataset is simulated for software development and testing. The readings are not collected from physical sensors.

## 7. Irrigation Logic

The system uses a predefined soil moisture threshold of 40%.

- If soil moisture is below 40%, the pump status is set to **ON**.
- If soil moisture is 40% or above, the pump status is set to **OFF**.

This threshold is an initial testing value and will require calibration for actual agricultural conditions.

## 8. Project Files

- `app.py` – Streamlit dashboard.
- `irrigation_logic.py` – Irrigation decision-making function.
- `clean_dataset.py` – Dataset cleaning and validation.
- `data_analysis.py` – Dataset analysis and statistical summary.
- `test_cases.py` – Tests for irrigation decision logic.
- `test_dataset.py` – Dataset-related testing.
- `irrigation_data_55.csv` – Original simulated dataset.
- `cleaned_irrigation_data.csv` – Cleaned dataset.
- `analyzed_irrigation_data.csv` – Analysed dataset.
- `SOFTWARE_TESTING.md` – Software testing documentation.
- `results/` – Contains analysis outputs and testing screenshots.

## 9. Installation and Execution

### Prerequisites

Install Python and ensure that it is available from your terminal.

### Step 1: Clone the Repository

```bash
git clone https://github.com/manishsingh770/solar-powered-smart-irrigation-system.git
cd solar-powered-smart-irrigation-system
```

### Step 2: Install Dependencies

```bash
pip install streamlit pandas matplotlib
```

### Step 3: Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser. If it does not open automatically, use the local URL displayed in the terminal.

**Important:** Run the dashboard from the directory containing `app.py` and the required cleaned dataset.

## 10. Testing and Results

The current software prototype has been tested using five different soil moisture values. All five test cases passed successfully.

The dataset analysis produced the following results:

- Total simulated readings: 55
- Average soil moisture: 45.35%
- Readings below the 40% threshold: 21
- Readings at or above the 40% threshold: 34
- Missing values: None in the analysed dataset
- Duplicate records: None in the analysed dataset

These results describe the current simulated dataset and do not represent measured field performance.

## 11. Current Project Status

**Completed:**
- Dataset creation.
- Dataset cleaning and validation.
- Python-based irrigation decision logic.
- Interactive Streamlit dashboard.
- Preliminary data analysis.
- Testing of five irrigation logic cases.

**Pending:**
- Integration with physical hardware.
- Testing with real soil moisture sensor readings.
- Solar panel and battery performance evaluation.
- Physical water pump control and system validation.

## 12. Future Scope

- Integrate an Arduino UNO and capacitive soil moisture sensor.
- Connect the solar panel, battery, and water pump.
- Replace simulated readings with real sensor data.
- Evaluate water usage and system reliability under practical conditions.
- Add real-time monitoring and data logging if required.

## 13. Conclusion

The project currently demonstrates a software prototype for threshold-based irrigation using Python and Streamlit. The dashboard helps visualize soil moisture data and simulate pump decisions. Future hardware integration and real-world testing will be required to evaluate its practical effectiveness.

## 14. Project Repository

GitHub: https://github.com/manishsingh770/solar-powered-smart-irrigation-system
