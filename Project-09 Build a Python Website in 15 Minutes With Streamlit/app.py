# PROJECT 9 : Build a Python Website in 15 Minutes With Streamlit

# Description: This project is a simple interactive data dashboard built using Streamlit. It allows users to upload a CSV file, filter the data, and visualize it using line charts.

# Author: AREEBA TANVEER AWAN

import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Awesome Hub", page_icon="✨", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #f5f5f5;
    }
    .main {
        background-color: darkblue;
        color: #f5f5f5;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(255,255,255,0.2);
        margin: 1rem;
    }
    .big-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 3.5rem;
        color: #ffb703;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.8rem;
        color: #8ecae6;
        text-align: center;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #f5f5f5;
        background-color: darkblue; 
        padding: 1rem;
        border-top: 1px solid #666;
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Quick Access")
page = st.sidebar.radio("Choose a page", ["Home", "Portfolio", "Contact"])

# Home Page
if page == "Home":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Welcome to Awesome Hub!</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Unleashing creativity through innovation.</p>", unsafe_allow_html=True)
  # For displaying images with updated parameter
    st.image("https://picsum.photos/1200/400", use_container_width=True, caption="Explore Endless Possibilities")

    st.write("""
        Dive into the world of cutting-edge design and seamless functionality. 
        Use the sidebar to explore my portfolio or reach out!
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Portfolio Page
elif page == "Portfolio":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>My Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Projects & Achievements</p>", unsafe_allow_html=True)
    st.image("https://picsum.photos/800/300", use_container_width=True, caption="Snapshot of Innovation")
    st.write("""
        Here's a glimpse of some of my finest creations:
        - **Project A:** Revolutionizing user experience.
        - **Project B:** Innovative solutions for modern problems.
        - **Project C:** Blending art with technology.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Page
elif page == "Contact":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Contact Me</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Let's create something amazing together!</p>", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        urgency = st.selectbox("How urgent is your message?", ["Low", "Normal", "High"])
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thanks, {name}! I'll get back to you soon.")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Built with ❤ and passion by Areeba Awan</div>", unsafe_allow_html=True)
