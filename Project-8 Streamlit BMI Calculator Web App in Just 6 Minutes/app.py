# PROJECT : 8 STREAMLIT BMI CALCULATOR WEB APP IN 6 MINUTES

# AUTHOR  : areeba Tanveer Awan

# DESCRIPTION : This is a simple BMI calculator web app using streamlit.
# It takes user input for height and weight, calculates BMI, and displays the result.

import streamlit as st

# Configure the page
st.set_page_config(page_title="Enhanced BMI Calculator", page_icon="🏋️", layout="centered")

# Title and description
st.title("🏋️ Enhanced BMI Calculator")
st.write("Track your Body Mass Index (BMI) effortlessly and gain personalized health insights! 🌟")

# Collect user input
st.sidebar.title("Input Your Details")
height = st.sidebar.number_input("📏 Enter your height (in meters):", min_value=0.1, format="%.2f")
weight = st.sidebar.number_input("⚖️ Enter your weight (in kilograms):", min_value=1.0, format="%.2f")

# Add a fun motivational message
st.sidebar.markdown("---")
st.sidebar.info("📋 This BMI Calculator is for informational purposes only and not a substitute for professional medical advice.")

# Calculate BMI when the button is clicked
if st.sidebar.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.subheader(f"🌟 Your BMI: {bmi:.2f}")

        # Provide insights based on BMI value
        if bmi < 18.5:
            st.warning("⚠️ You're underweight. Consider consulting a nutritionist for a healthy diet plan. 🥗")
            st.image("https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif", caption="Healthy meals make a difference!")
        elif 18.5 <= bmi < 24.9:
            st.success("🎉 You have a normal weight! Keep up the great work! 💪")
            st.balloons()
        elif 25 <= bmi < 29.9:
            st.info("⚡ You're overweight. Regular physical activity could help! 🏃‍♀️")
            st.image("https://media.giphy.com/media/l3q2ty5p05Fr1Wgq8/giphy.gif", caption="Stay active and stay strong!")
        else:
            st.error("🚨 You're obese. It's recommended to consult a healthcare provider for guidance. 🩺")
            st.image("https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif", caption="Your health is your wealth!")

    else:
        st.error("❌ Please provide valid height and weight.")

# Footer for additional details
st.markdown("---")
st.write("💡 **Tip**: A balanced diet and regular exercise are keys to a healthy lifestyle!")
st.write("Created with ❤️ by Areeba Tanveer Awan")

#📋 This BMI Calculator is for informational purposes only and not a substitute for professional medical advice.
# ------------------------ FINISHED ------------------------