import numpy as np
import pandas as pd 
import pickle
import streamlit as st

# Lode the model 
model = pickle.load(open("model.pkl", "rb"))

data = pd.read_csv("Crop_recommendation.csv")

n = st.number_input('Enter N')
p = st.number_input('Enter P')
k = st.number_input('Enter K')
temp = st.number_input('Enter Temp')
hum = st.number_input('Enter Humidity')
ph = st.number_input('Enter ph')
rain = st.number_input('Enter rainfall')

input = pd.DataFrame([[n , p , k , temp , hum , ph , rain]] , columns=['N','P','K','temperature','humidity','ph','rainfall'])

if st.button("Predict"):
    result = model.predict(input)
    st.write("Prediction:", result)