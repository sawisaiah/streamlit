import streamlit as st

def calculate_bmi(height_ft, height_in, weight_lb):
    height = (height_ft * 12) + height_in
    bmi = (weight_lb / (height ** 2)) * 703
    return bmi

# Streamlit App
st.title("BMI Calculator")

# Input fields for height and weight
height_ft = st.number_input("Enter your height (feet):", min_value=1, value=5)
height_in = st.number_input("Enter your height (inches):", min_value=0, max_value=11, value=6)
weight_lb = st.number_input("Enter your weight (pounds):", min_value=1, value=150)

# Calculate BMI and display the result
if st.button("Calculate BMI"):
    bmi = calculate_bmi(height_ft, height_in, weight_lb)
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
