import streamlit as st
import pickle
import numpy as np

# Load trained demo model and selected feature names
model = pickle.load(open("streamlit_model.pkl", "rb"))
selected_features = pickle.load(open("streamlit_features.pkl", "rb"))

st.title("Bankruptcy Prediction App")
st.write("Enter the financial values to predict bankruptcy risk.")

user_inputs = []

for feature in selected_features:
    value = st.number_input(feature, value=0.0)
    user_inputs.append(value)

inputs = np.array([user_inputs])

if st.button("Predict"):
    prediction = model.predict(inputs)
    probability = model.predict_proba(inputs)[0][1]

    st.write(f"Bankruptcy Risk Score: {probability:.2%}")

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Bankruptcy")
    else:
        st.success(" Company is Financially Healthy")