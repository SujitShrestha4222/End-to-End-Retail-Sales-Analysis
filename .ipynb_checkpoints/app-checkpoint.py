# ==============================
# Retail Sales Prediction App
# ==============================

import streamlit as st
import pandas as pd
import joblib

from analysis import category_lst



# Load trained model
model = joblib.load("model.pkl")




# App title
st.title("📊 Retail Sales Prediction App")

st.write("Enter order details to predict estimated sales.")




# User inputs for Category and Sub-category Selector
category_data = {
    "Technology": category_lst,
    "Furniture": ["Bookcase", "Chair", "Table"],
    "Clothing": ["Shirt", "Pant", "Shoes"]
}

category = st.selectbox(
    "Select Category",
    list(category_data.keys())
)

sub_category = st.selectbox(
    "Select Sub-category",
    category_data[category]
)

st.write("You selected:")
st.write("Category:", category)
st.write("Sub-category:", sub_category)





# User inputs for others remaining
region = st.selectbox("Region", ["Central", "East", "South", "West"])

segment = st.selectbox("Customer Segment", ["Consumer", "Corporate", "Home Office"])

ship_mode = st.selectbox(
    "Ship Mode",
    ["First Class", "Same Day", "Second Class", "Standard Class"]
)

# Date-based inputs
order_year = st.number_input("Order Year", min_value=2014, max_value=2030, value=2018)
order_month = st.slider("Order Month", 1, 12, 6)
order_day = st.slider("Order Day", 1, 31, 15)

# Predict button
if st.button("Predict Sales"):

    input_data = pd.DataFrame({
        "Category": [category],
        "Sub-Category": [sub_category],
        "Region": [region],
        "Segment": [segment],
        "Ship Mode": [ship_mode],
        "Order Month": [order_month],
        "Order Day": [order_day],
        "Order Year": [order_year]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: {prediction[0]:.2f}")




    ### streamlit run app.py