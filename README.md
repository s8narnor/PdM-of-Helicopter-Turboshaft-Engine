# 🚁 Predictive Maintenance of Helicopter Turboshaft Engines

This project demonstrates the use of machine learning for predictive maintenance of **helicopter turboshaft engines**. We use classification techniques to detect faults in engine operation, enabling proactive maintenance and minimizing downtime.

The goal is to:

- Detect potential failures or faults in turboshaft engines before they occur
- Minimize unplanned downtime
- Reduce maintenance costs and risk
- Increase operational efficiency and safety

---

## 📊 Project Overview

This end-to-end notebook includes:

- ✅ Data Loading & Exploration  
- ✅ Fault Label Encoding  
- ✅ Train-Test Splitting  
- ✅ Class Imbalance Handling using **SMOTE**  
- ✅ Model Training using **Random Forest Classifier**  
- ✅ Evaluation using Accuracy, F1 Score, Confusion Matrix  
- ✅ Deployment using **Streamlit**

---

## 📁 Dataset

The project uses a dataset with labeled engine data indicating normal and multiple faulty conditions. Each instance represents sensor readings and other operational parameters.
The data file contains real-time sensor data collected from helicopter turboshaft engines for fault detection and predictive maintenance. It includes hourly readings from March 1, 2024, to December 31, 2024, capturing key engine parameters such as temperature, pressure, vibration, speed, and fuel flow.

> **Note:** Dataset is sourced from an open-access Helicopter Turboshaft Fault Detection archive. Dataset: [C-MAPSS Helicopter Engine Dataset](https://www.kaggle.com/datasets/ziya07/helicopter-turboshaft-detection-dataset)


---

## 🧪 Model Summary

- Classifier: `RandomForestClassifier`
- Imbalance Handling: `SMOTE` (Synthetic Minority Over-sampling Technique)
- Evaluation: Accuracy, Recall, Precision, Confusion Matrix
- Deployment: Built using **Streamlit** for easy web-based access

---

## 🧠 Key Learnings
- SMOTE significantly improves recall for minority fault classes
- Class imbalance handling is crucial for real-world fault detection

---

## 🚀 Run Locally

```bash

### 1. Clone the repo

git clone https://github.com/s8narnor/pdm-turboshaft-helicopter.git
cd pdm-turboshaft-helicopter

### 2. Install dependencies

Copy
Edit
pip install -r requirements.txt

### 3. Run the Streamlit App

Copy
Edit
streamlit run app.py
