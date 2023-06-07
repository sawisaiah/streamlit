
import streamlit as st

def calculate_bmi(height, weight):
    bmi = weight / (height / 100) ** 2
    return bmi

# Streamlit App
st.title("BMI Calculator")

# Input fields for height and weight
height = st.number_input("Enter your height (in cm):", min_value=1.0, step=0.1)
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, step=0.1)

# Calculate BMI and display the result
if st.button("Calculate BMI"):
    bmi = calculate_bmi(height, weight)
    st.write("Your BMI is {:.2f}".format(bmi))

    # Provide interpretation of BMI category
    if bmi < 18.5:
        st.write("Category: Underweight")
    elif 18.5 <= bmi < 25:
        st.write("Category: Normal weight")
    elif 25 <= bmi < 30:
        st.write("Category: Overweight")
    else:
        st.write("Category: Obesity")
