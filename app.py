
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Solar Smart Irrigation",
    page_icon="🌱",
    layout="wide"
)

# Title
st.title("🌱 Solar-Powered Smart Irrigation System")
st.write(
    "A software prototype for soil-moisture-based irrigation."
)

st.info(
    "Simulation mode: data and pump decisions are simulated. "
    "No physical hardware is connected."
)

# Load cleaned data
data = pd.read_csv("cleaned_irrigation_data.csv")

# Interactive threshold
threshold = st.slider(
    "Soil Moisture Threshold (%)",
    min_value=10,
    max_value=80,
    value=40
)

# Recalculate pump status
data["pump_status"] = data["soil_moisture"].apply(
    lambda moisture: "ON" if moisture < threshold else "OFF"
)

# Summary calculations
latest = data.iloc[-1]
average_moisture = data["soil_moisture"].mean()
irrigation_count = int(
    (data["soil_moisture"] < threshold).sum()
)
off_count = len(data) - irrigation_count

# Summary cards
st.subheader("System Overview")

c1, c2, c3 = st.columns(3)

c1.metric("Total Readings", len(data))
c2.metric("Average Moisture", f"{average_moisture:.1f}%")
c3.metric("Readings Below Threshold", irrigation_count)

# Current simulated status based on the latest record
st.subheader("Latest Simulated Pump Status")

if latest["soil_moisture"] < threshold:
    st.error(
        f"PUMP ON — latest moisture is "
        f"{latest['soil_moisture']}%."
    )
else:
    st.success(
        f"PUMP OFF — latest moisture is "
        f"{latest['soil_moisture']}%."
    )

st.caption(
    f"Latest record: {latest['time']}. "
    "This is a simulated decision, not a real pump command."
)

# Moisture chart
st.subheader("Soil Moisture Monitoring")

fig, ax = plt.subplots(figsize=(12, 4))

ax.plot(
    data["time"],
    data["soil_moisture"],
    marker="o",
    label="Soil Moisture"
)

ax.axhline(
    threshold,
    linestyle="--",
    label="Threshold"
)

ax.set_xlabel("Time")
ax.set_ylabel("Soil Moisture (%)")
ax.set_ylim(0, 100)
ax.tick_params(axis="x", rotation=60)
ax.grid(True)
ax.legend()
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Pie chart
st.subheader("Irrigation Decision Distribution")

fig2, ax2 = plt.subplots()

ax2.pie(
    [irrigation_count, off_count],
    labels=["Below Threshold", "At/Above Threshold"],
    autopct="%1.1f%%",
    startangle=90
)

ax2.axis("equal")
st.pyplot(fig2)
plt.close(fig2)

# Data table
st.subheader("Cleaned Irrigation Dataset")
st.dataframe(data, use_container_width=True)

# Download cleaned data with current simulated decisions
csv_data = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Dataset CSV",
    data=csv_data,
    file_name="irrigation_dashboard_data.csv",
    mime="text/csv"
)

# Explanation
with st.expander("How does the system work?"):
    st.write("""
    1. The dataset provides soil-moisture readings.
    2. Python compares each reading with the selected threshold.
    3. If moisture is below the threshold, the simulated pump status is ON.
    4. Otherwise, the simulated pump status is OFF.
    5. The dashboard displays the readings and decisions.

    Solar availability is recorded in the dataset but is not currently
    used to control the pump.
    """)

st.caption(
    "Future work: Arduino UNO integration, physical sensor calibration, "
    "solar power testing, battery testing and water-flow measurement."
)
