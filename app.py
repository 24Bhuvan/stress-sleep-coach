import streamlit as st
import pandas as pd
import joblib

from utils.rules import get_stress_tip, get_sleep_tip

MODEL_PATH = "model.pkl"


# -----------------------------
# Load model (cached)
# -----------------------------
@st.cache_resource
def load_models():
    return joblib.load(MODEL_PATH)


models = load_models()
stress_model = models["stress_model"]
sleep_model = models["sleep_model"]


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Stress & Sleep Coach", layout="centered")
st.title("Stress & Sleep Coach Bot")

st.header("Enter Your Details")

gender = st.selectbox("Gender", ["Male", "Female"])

age = st.number_input("Age", min_value=18, max_value=80, value=30)

occupation = st.selectbox(
    "Occupation",
    [
        "Software Engineer", "Doctor", "Sales Representative",
        "Teacher", "Engineer", "Accountant",
        "Scientist", "Lawyer", "Nurse",
        "Salesperson", "Manager"
    ],
)

sleep_duration = st.number_input(
    "Sleep Duration (hours)", min_value=3.0, max_value=12.0, value=7.0
)

physical_activity = st.number_input(
    "Physical Activity Level", min_value=0, max_value=100, value=50
)

bmi_category = st.selectbox(
    "BMI Category",
    ["Normal", "Normal Weight", "Overweight", "Obese"]
)


# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    input_df = pd.DataFrame(
        {
            "Gender": [gender],
            "Age": [age],
            "Occupation": [occupation],
            "Sleep Duration": [sleep_duration],
            "Physical Activity Level": [physical_activity],
            "BMI Category": [bmi_category],
        }
    )

    stress_pred = stress_model.predict(input_df)[0]
    sleep_pred = sleep_model.predict(input_df)[0]

    st.subheader("Prediction Results")
    st.write(f"Stress Level: **{stress_pred}**")
    st.write(f"Sleep Quality: **{sleep_pred}**")

    st.subheader("Recommendations")
    st.write(get_stress_tip(stress_pred))
    st.write(get_sleep_tip(sleep_pred))