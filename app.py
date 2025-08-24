# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and label encoder
model = joblib.load("helicopter_fault_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🚁 Helicopter Turboshaft Fault Detection")
st.write("This demo uses a trained Random Forest model to detect possible engine faults based on sensor data.")

# Input fields
with st.form("fault_form"):
    st.subheader("Enter Helicopter Sensor Data")
    temp_compressor = st.number_input("Temp_Compressor", value=0.5)
    temp_turbine = st.number_input("Temp_Turbine", value=0.0)
    pressure_compressor = st.number_input("Pressure_Compressor", value=1.0)
    vibration_compressor = st.number_input("Vibration_Compressor", value=0.4)
    speed_turbine = st.number_input("Speed_Turbine", value=1.1)
    fuel_flow = st.number_input("Fuel_Flow", value=0.25)
    altitude = st.number_input("Altitude", value=0.0)
    airspeed = st.number_input("Airspeed", value=0.9)
    ambient_temp = st.number_input("Ambient_Temp", value=0.5)
    
    submitted = st.form_submit_button("Predict Fault")

if submitted:
    input_data = pd.DataFrame({
        'Temp_Compressor': [temp_compressor],
        'Temp_Turbine': [temp_turbine],
        'Pressure_Compressor': [pressure_compressor],
        'Vibration_Compressor': [vibration_compressor],
        'Speed_Turbine': [speed_turbine],
        'Fuel_Flow': [fuel_flow],
        'Altitude': [altitude],
        'Airspeed': [airspeed],
        'Ambient_Temp': [ambient_temp]
    })

    prediction = model.predict(input_data)
    pred_label = label_encoder.inverse_transform(prediction)

    st.success(f"Predicted Fault: **{pred_label[0]}**")
