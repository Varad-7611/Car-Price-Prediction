import streamlit as st
import pandas as pd
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("car_price_model.pkl")

model = load_model()

# Load data for dropdown options
@st.cache_data
def load_data():
    df = pd.read_csv("Car Sales.xlsx - car_data.csv")
    df = df[['Company', 'Model', 'Transmission', 'Price ($)']].dropna()
    return df

df = load_data()

# Streamlit UI
st.title("🚘 Car Price Prediction")
st.write("Predict the price of a car based on company, model, and transmission type.")

# Input: Company
company = st.selectbox("Select Car Company", df['Company'].unique())

# Input: Model (filtered by company)
models = df[df['Company'] == company]['Model'].unique()
model_name = st.selectbox("Select Car Model", models)

# Input: Transmission
transmission = st.selectbox("Select Transmission Type", df['Transmission'].unique())

# Predict on button click
if st.button("Predict Price"):
    input_df = pd.DataFrame([[company, model_name, transmission]],
                            columns=['Company', 'Model', 'Transmission'])
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Car Price: **${int(prediction):,}**")
