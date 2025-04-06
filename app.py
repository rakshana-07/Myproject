import streamlit as st
import pandas as pd
import datetime

# App Title
st.set_page_config(page_title="Smart Air Quality Monitor", layout="wide")
st.title("AI-Powered Smart Indoor Air Quality Monitoring System")

st.markdown("Monitor and visualize real-time air quality data with AI insights.")

# Simulated Sensor Data (you can replace this with actual data later)
data = pd.DataFrame({
    "Timestamp": pd.date_range(datetime.datetime.now(), periods=5, freq='H'),
    "PM2.5 (µg/m³)": [25, 35, 30, 28, 40],
    "PM10 (µg/m³)": [45, 55, 60, 50, 65],
    "CO (ppm)": [0.5, 0.6, 0.7, 0.65, 0.8],
    "Humidity (%)": [45, 50, 48, 52, 47],
    "Temperature (°C)": [24, 25, 25.5, 26, 24.5]
})

# Data Table
st.subheader("Air Quality Data")
st.dataframe(data)

# Line Chart
st.subheader("Trend Analysis")
st.line_chart(data.set_index("Timestamp"))

# Summary Metrics
st.subheader("Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Average PM2.5", f"{data['PM2.5 (µg/m³)'].mean():.1f} µg/m³")
col2.metric("Average CO", f"{data['CO (ppm)'].mean():.2f} ppm")
col3.metric("Average Temp", f"{data['Temperature (°C)'].mean():.1f} °C")

# AI Recommendation Logic (Mock)
st.subheader("AI Recommendation")
if data['PM2.5 (µg/m³)'].iloc[-1] > 35:
    st.error("Poor air detected! Turn on air purifier and ventilate the room.")
else:
    st.success("Air quality is good. No action needed.")

st.markdown("---")
st.caption("Developed by Rakshana M | Smart Air App")
