import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("battery_capacity_model.pkl")

st.set_page_config(
    page_title="Battery Health Estimator",
    page_icon="🔋",
    layout="centered"
)

st.title("🔋 Battery SOH Prediction System")

with st.expander("About This Project"):

    st.write("""
    This application predicts lithium-ion battery capacity
    and estimates battery health using Machine Learning.

    The model analyzes battery operating characteristics
    such as voltage, current, temperature, and discharge
    behavior to estimate remaining battery capacity.
    """)




st.info(
    "You can either upload a battery CSV file or enter battery measurements manually."
)

tab1, tab2, tab3 = st.tabs(
    [
        "📂 Upload CSV",
        "⚙️ Advanced Input",
        "👤 Quick Health Check"
    ]
)


def show_result(prediction):

    health_percent = min(max((prediction / 2.0) * 100, 0), 100)

    if health_percent >= 90:
        status = "Excellent"
        recommendation = "Battery is operating in excellent condition."

    elif health_percent >= 75:
        status = "Good"
        recommendation = "Battery health is good. No action required."

    elif health_percent >= 50:
        status = "Moderate"
        recommendation = "Battery shows signs of degradation. Monitor performance."

    else:
        status = "Poor"
        recommendation = "Battery health is poor. Replacement may be required."

    st.success(f"Estimated Capacity: {prediction:.3f} Ah")

    st.metric(
        "Battery Health",
        f"{health_percent:.1f}%"
    )

    st.progress(int(health_percent))

    st.subheader(f"Status: {status}")

    st.write("### Recommendation")
    st.write(recommendation)


# =========================
# CSV UPLOAD TAB
# =========================

with tab1:

    st.subheader("Upload Battery Cycle Data")

    uploaded_file = st.file_uploader(
        "Choose a battery CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:
            sample = pd.read_csv(uploaded_file)

            features = pd.DataFrame([{
                "mean_voltage": sample["Voltage_measured"].mean(),
                "max_voltage": sample["Voltage_measured"].max(),
                "min_voltage": sample["Voltage_measured"].min(),
                "mean_temperature": sample["Temperature_measured"].mean(),
                "max_temperature": sample["Temperature_measured"].max(),
                "mean_current": sample["Current_measured"].mean(),
                "duration": sample["Time"].max()
            }])

            prediction = model.predict(features)[0]

            show_result(prediction)

        except Exception:
            st.error(
                "Invalid file format. Please upload a battery cycle CSV file."
            )


# =========================
# MANUAL INPUT TAB
# =========================

with tab2:

    st.subheader("Advanced Battery Measurements")

    voltage = st.number_input(
        "Battery Voltage (V)",
        value=3.7,
        help="Current voltage level of the battery"
    )

    temperature = st.number_input(
        "Battery Temperature (°C)",
        value=30.0,
        help="Current operating temperature"
    )

    current = st.number_input(
        "Battery Current (A)",
        value=1.0,
        help="Amount of current being used"
    )

    duration = st.number_input(
        "Battery Usage Duration (seconds)",
        value=5000.0,
        help="How long the battery has been discharging"
    )

    if st.button("Analyze Battery"):

        features = pd.DataFrame([{
    "mean_voltage": voltage,
    "max_voltage": voltage + 0.3,
    "min_voltage": voltage - 0.5,
    "mean_temperature": temperature,
    "max_temperature": temperature + 5,
    "mean_current": current,
    "duration": duration
}])

        prediction = model.predict(features)[0]

        show_result(prediction)
# =========================
# QUICK HEALTH CHECK
# =========================

with tab3:

    st.subheader("Quick Battery Health Check")

    battery_age = st.slider(
        "Battery Age (Months)",
        0,
        60,
        12
    )

    usage_hours = st.slider(
        "Daily Usage (Hours)",
        1,
        16,
        6
    )

    drains_fast = st.radio(
        "Does the battery drain quickly?",
        ["No", "Yes"]
    )

    gets_hot = st.radio(
        "Does the device become hot during use?",
        ["No", "Yes"]
    )

    if st.button("Check Battery Health"):

        score = 100

        score -= battery_age * 0.8

        score -= usage_hours * 2

        if drains_fast == "Yes":
            score -= 25

        if gets_hot == "Yes":
            score -= 20

        score = max(0, min(100, score))

        if score >= 80:
            status = "Excellent"

        elif score >= 60:
            status = "Good"

        elif score >= 40:
            status = "Moderate"

        else:
            status = "Poor"

        st.metric(
            "Estimated Health Score",
            f"{score:.0f}%"
        )

        st.progress(int(score))

        st.subheader(f"Status: {status}")
st.divider()

st.caption(
    "Dataset Source: NASA Prognostics Center of Excellence Battery Dataset"
)