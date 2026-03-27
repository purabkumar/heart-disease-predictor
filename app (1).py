import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("❤️ Heart Disease Prediction System")

st.markdown("### Enter Patient Details")

# Inputs with full names
age = st.number_input("Age", 20, 100)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 0 if sex == "Female" else 1

cp = st.selectbox("Chest Pain Type", [
    "Typical Angina",
    "Atypical Angina",
    "Non-anginal Pain",
    "Asymptomatic"
])
cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp) + 1

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200)

chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Resting Electrocardiographic Results", [
    "Normal",
    "ST-T wave abnormality",
    "Left ventricular hypertrophy"
])
restecg = ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"].index(restecg)

thalach = st.number_input("Maximum Heart Rate Achieved", 60, 220)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 6.0)

slope = st.selectbox("Slope of Peak Exercise ST Segment", [
    "Upsloping",
    "Flat",
    "Downsloping"
])
slope = ["Upsloping", "Flat", "Downsloping"].index(slope) + 1

ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])

thal = st.selectbox("Thalassemia", [
    "Normal",
    "Fixed Defect",
    "Reversible Defect"
])
thal_map = {
    "Normal": 3,
    "Fixed Defect": 6,
    "Reversible Defect": 7
}
thal = thal_map[thal]

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
