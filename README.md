# Battery SOH Prediction

A machine learning-based application for estimating the State of Health (SOH) and remaining capacity of lithium-ion batteries using battery operating characteristics.

## Project Overview

This project analyzes battery discharge behavior and predicts battery capacity using machine learning techniques. The predicted capacity is then used to estimate overall battery health and provide a user-friendly health assessment.

The application includes:

* CSV-based battery analysis
* Advanced technical input mode
* Quick battery health assessment
* Interactive Streamlit web interface

## Features

* Battery State of Health (SOH) Prediction
* Capacity Estimation
* CSV Upload and Analysis
* Advanced Battery Input Mode
* Quick Health Check
* Interactive Dashboard using Streamlit

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib

## Machine Learning Models

The following models were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

Random Forest achieved the best performance and was selected for deployment.

## Project Workflow

Battery Data
→ Data Preprocessing
→ Feature Extraction
→ Model Training
→ Capacity Prediction
→ SOH Estimation
→ Health Assessment

## Application Modules

### CSV Upload

Allows users to upload battery cycle data and obtain battery health predictions automatically.

### Advanced Input

Allows technical users to enter battery measurements manually.

### Quick Health Check

Provides a simple battery assessment based on user-friendly inputs.

## Future Enhancements

* Real-time battery monitoring
* IoT-based battery data collection
* Mobile application integration
* Remaining Useful Life (RUL) prediction

## Author

MadhuMita Rachakonda
