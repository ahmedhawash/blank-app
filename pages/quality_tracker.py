import os
import streamlit as st
import pandas as pd

st.title("Quality Tracker")
st.header("Quality Results", divider="gray")

# Questions Path
SAVE_PATH = "data/questions"

current_questions_csv_path = os.path.join(SAVE_PATH, os.listdir(SAVE_PATH)[0])
current_questions_df = pd.read_csv(current_questions_csv_path)




with st.form("my_form"):

    q1 = st.radio(
        "**Q1. Is everything OK?**",
        ["Yes", "No"],
        horizontal=True,
        index=None,
        key="q1"
    )
    col1, col2 = st.columns(2)
    with col1:
        q1weight = st.text_input("Weight", "20", disabled=True )
    with col2:
        q1score = st.text_input("Score","0",disabled=True)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(q1)

