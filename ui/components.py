# This file will contain Streamlit UI components like input boxes, buttons, etc.

import streamlit as st

def get_user_inputs():
    gender = st.selectbox("Gender of the child:", ["male", "female"], key="gender_selectbox")
    name = st.text_input("Child's Name:")
    age = st.number_input("Child's Age:", min_value=2)
    situation = st.text_input("Describe the situation:")
    return gender, name, age, situation

def display_header():
    st.header('Social Story Generator 🧩')
    st.write(f"🧠 Using model: claude_2")
