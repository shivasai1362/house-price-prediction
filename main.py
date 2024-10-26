from joblib import load
import streamlit as st

model = load("model.joblib")

st.title("House Price Prediction")
st.write("Enter Area, Bedroom, No of stories, Is it at mainroad? ")


col1, col2, col3, col4 = st.columns(4)

area = 0
bedroom = 0
stories = 0
mainroad = 0

with col1:
    area = st.number_input("Area", min_value=1000, max_value=18000, step=1)
with col2:
    bedroom = st.number_input("Bedroom", min_value=1, max_value=4, step=1)
with col3:
    stories = st.number_input("No of stories", min_value=1, max_value=4, step=1)
with col4:
    mainroad = st.selectbox("Is it at mainroad?", ["Yes", "No"])
    if mainroad == "Yes":
        mainroad = 1
    else:
        mainroad = 0
    
predict = st.button("Predict Price")
if predict:
    price = model.predict([[area, bedroom, stories, mainroad]])
    st.success(f"Predicted Price: {price[0]:.2f}")