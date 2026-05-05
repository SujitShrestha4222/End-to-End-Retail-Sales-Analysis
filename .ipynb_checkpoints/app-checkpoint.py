# ==============================
# Retail Sales Prediction App
# ==============================
import streamlit as st
import pandas as pd
import joblib


# These variables are coming from data_store.py file which we made basically to get the requried datas for our app
from data_store import category_lst, region_lst, segment_lst, shipmode_lst
from data_store import category_dict



# Load trained model
model = joblib.load("../data/model_RandomForestRegressor.pkl")






# App title
st.title("📊 Retail Sales Prediction App")
st.write("Enter order details to predict estimated sales.")






# User inputs for category and sub_category Selector using our dictionary (i.e category_dict)
# where,
# key contains categories
# value contains sub_categories

category = st.selectbox(
    "Select Category",
    list(category_dict.keys())  #converting key values of category_dict in list(so, it's list of category)
)

sub_category = st.selectbox(
    "Select Sub-category",
    category_dict[category]     # means automatically updating the sub-categories based on chosed category
)

st.write("You have selected:")
st.write("Category:", category)
st.write("Sub-category:", sub_category)





# User inputs for others remaining
region = st.selectbox("Region", region_lst)

segment = st.selectbox("Customer Segment", segment_lst)

ship_mode = st.selectbox("Ship Mode", shipmode_lst)

# # Date-based inputs   (COMMENTING IT AS USING THE OLD_MODEL ONLY WHICH DON'T HAVE THESE)
# order_year = st.number_input("Order Year", min_value=2014, max_value=2030, value=2018)
# order_month = st.slider("Order Month", 1, 12, 6)
# order_day = st.slider("Order Day", 1, 31, 15)

# Predict button
if st.button("Predict Sales"):

    input_data = pd.DataFrame({
        "Category": [category],
        "Sub-Category": [sub_category],
        "Region": [region],
        "Segment": [segment],
        "Ship Mode": [ship_mode],
        "Order Year": [order_year],
        "Order Month": [order_month],
        "Order Day": [order_day]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: {prediction[0]:.2f}")




    ### streamlit run app.py