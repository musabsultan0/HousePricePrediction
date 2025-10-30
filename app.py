import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="🏠 House Price Prediction", layout="centered")

st.title("🏠 House Price Prediction App")
st.subheader("Enter House Details:")

# Input fields according to model features
LotArea = st.number_input("Lot Area (sq ft):", min_value=100, max_value=100000, value=5000)
OverallQual = st.slider("Overall Quality (1-10):", 1, 10, 5)
OverallCond = st.slider("Overall Condition (1-10):", 1, 10, 5)
YearBuilt = st.number_input("Year Built:", min_value=1800, max_value=2025, value=2000)
GrLivArea = st.number_input("Ground Living Area (sq ft):", min_value=100, max_value=10000, value=1500)
FullBath = st.number_input("Number of Full Bathrooms:", min_value=0, max_value=5, value=2)
BedroomAbvGr = st.number_input("Number of Bedrooms Above Ground:", min_value=0, max_value=10, value=3)
KitchenAbvGr = st.number_input("Number of Kitchens Above Ground:", min_value=0, max_value=5, value=1)
TotRmsAbvGrd = st.number_input("Total Rooms Above Ground:", min_value=1, max_value=20, value=7)
Fireplaces = st.number_input("Number of Fireplaces:", min_value=0, max_value=5, value=1)
GarageCars = st.number_input("Garage Capacity (Cars):", min_value=0, max_value=10, value=2)
GarageArea = st.number_input("Garage Area (sq ft):", min_value=0, max_value=2000, value=500)
Neighborhood_RL = st.selectbox("Neighborhood RL (1 if RL, else 0):", [0, 1])

# Convert inputs to numpy array
input_data = np.array([[LotArea, OverallQual, OverallCond, YearBuilt, GrLivArea,
                        FullBath, BedroomAbvGr, KitchenAbvGr, TotRmsAbvGrd,
                        Fireplaces, GarageCars, GarageArea, Neighborhood_RL]])

# Predict button
if st.button("🔍 Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"🏡 Predicted House Price: ${prediction[0]:,.2f}")
