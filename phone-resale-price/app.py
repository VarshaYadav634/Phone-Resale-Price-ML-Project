import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ------------------- Page Config -------------------
st.set_page_config(page_title="📱 Phone Resale Price Predictor", page_icon="📊", layout="centered")

# ------------------- Load Dataset & Model -------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/phone_prices.csv")

data = load_data()

with open("model/phone_resale_model.pkl", "rb") as f:
    model, le = pickle.load(f)

# ------------------- UI -------------------
st.title("📱 Phone Resale Price Prediction System")
st.write("Predict the **resale value of smartphones** using Machine Learning based on specifications and years of use.")

st.header("🧾 Enter Phone Specifications")
brand = st.selectbox("📱 Select Brand", data['brand'].unique())
ram = st.number_input("🔹 RAM (GB)", min_value=2, max_value=16, value=6, step=1)
storage = st.number_input("💾 Storage (GB)", min_value=32, max_value=512, value=128, step=32)
main_camera = st.number_input("📸 Main Camera (MP)", min_value=8, max_value=200, value=64, step=2)
front_camera = st.number_input("🤳 Front Camera (MP)", min_value=5, max_value=64, value=16, step=1)
original_price = st.number_input("💵 Original Price (₹)", min_value=5000, max_value=150000, value=30000, step=1000)
battery = st.slider("🔋 Battery (mAh)", 2000, 6000, 4500, step=100)
years_of_use = st.slider("📆 Years of Use", 0, 10, 2)

# Encode brand
brand_encoded = le.transform([brand])[0]

input_data = pd.DataFrame({
    'brand_encoded': [brand_encoded],
    'ram': [ram],
    'storage': [storage],
    'battery': [battery],
    'main_camera': [main_camera],
    'front_camera': [front_camera],
    'original_price': [original_price],
    'years_of_use': [years_of_use]
})

if st.button("💰 Predict Resale Price"):
    prediction = model.predict(input_data)
    resale_price = np.round(prediction[0], 2)
    st.success(f"📱 Estimated Resale Price: ₹{resale_price}")
    st.balloons()



# to run 
# 1. python train_model.py
# 2.streamlit run app.py