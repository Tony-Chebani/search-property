#!/usr/bin/env python
# coding: utf-8

# # <center><u>SIG720 Task 5D</u></center> #

# ## Dataset Schema ##

# This is a set of data created from imaginary data of house prices in the top three suburbs of Melbourne. The data acquisition leverages <b>Paris Housing Price Prediction – Kaggle </b> to automatically  collect at least 150 housing data points (at least 50 for each suburb). 
# 
# The goal of the task is to develop and evaluate various regression models to predict housing prices in Melbourne.
# 
# The data includes the following features as sourced from:
# 
# * <b>squareMeters</b>: size of house in square meters
# 
# * <b>numberOfRooms</b>: number of house rooms
# 
# * <b>hasYard</b>: does house include yard? 0 - no, 1 - yes
# 
# * <b>hasPool</b>: does house include a pool
# 
# * <b>floors</b>: how many floors are there
#  
# * <b>cityCode</b>: number of zip code
# 
# * <b>cityPartRange</b>: range from 0 - cheapest to 10 - the most expensive (the higher the range, the more exclusive the neighbourhood is) <br>
# 
# * <b>numPrevOwners</b>: number of previous owners <br>
# 
# * <b>made</b>: year made<br>
#     
# * <b>isNewBuilt</b>: is it new or renovated<br>
#      
# * <b>hasStormProtector</b>: 
# 
# * <b>basement</b>: basement square meters
# 
# * <b>attic</b>: attic square meters
# 
# * <b>garage</b>: garage size
# 
# * <b>hasStorageRoom</b>: 
# 
# * <b>hasGuestRoom</b>: number of guest rooms
# 
# * <b>price</b>: predicted value
# 
# 
# <b>Source:</b>https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction

# ### Importing the libraries ###

# In[25]:

#!pip install streamlit
import streamlit as st

# The VERY FIRST Streamlit command in the script
st.set_page_config(
    page_title="Melbourne House Price Predictor",
    page_icon="🏠",
    layout="centered",              # or "wide"
    initial_sidebar_state="auto"    # "auto", "expanded", or "collapsed"
)

st.set_page_config(
    page_title="Melbourne House Price Predictor",
    page_icon="🏠",
    layout="centered",              # Use "wide" if you prefer a full‐width layout
    initial_sidebar_state="auto"    # Options: "auto", "expanded", "collapsed"
)

def main():
    # App’s UI
    st.title("🏠 Melbourne House Price Predictor")
    st.write("Input the property details below and click **Predict**.")

    # ... add your input widgets, model inference, and results display here ...
    
    # Inputs
    cols = st.columns(2)
    with cols[0]:
        square_m = st.number_input("Living Area (sqm)", 10, 10000, 50)
        rooms     = st.number_input("Number of Rooms", 1, 20, 3)
        has_yard  = st.checkbox("Yard")
        has_pool  = st.checkbox("Pool")
        floors    = st.number_input("Floors", 1, 10, 1)
        city_code = st.number_input("City Code", 1, 99999, 50000)
        part_rng  = st.slider("Neighborhood Range (0–10)", 0, 10, 5)
        prev_own  = st.number_input("Previous Owners", 0, 10, 1)

    with cols[1]:
        year_built = st.number_input("Year Built", 1900, 2025, 2005)
        is_new     = st.checkbox("New / Renovated")
        has_storm  = st.checkbox("Storm Protector")
        basement   = st.number_input("Basement (sqm)", 0, 10000, 0)
        attic      = st.number_input("Attic (sqm)", 0, 10000, 0)
        garage     = st.number_input("Garage (sqm)", 0, 2000, 0)
        has_store  = st.checkbox("Storage Room")
        has_guest  = st.checkbox("Guest Room")

    # 4. Prediction
    if st.button("Predict Price"):
        x = np.array([[ 
            square_m, rooms, int(has_yard), int(has_pool), floors,
            city_code, part_rng, prev_own, year_built,
            int(is_new), int(has_storm), basement,attic, garage, int(has_store), int(has_guest)
    ]])

    x_scaled = scaler.transform(x)
    price    = model.predict(x_scaled)[0]
    st.success(f"Estimated Price: ${price:,.2f}")

    
    if __name__ == "__main__":
        main()