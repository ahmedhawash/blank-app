import streamlit as st

get_started_page = st.Page("get_started", title="Get Started", icon=":material/add_circle:")
quality_tracker_page = st.Page("quality_tracker.py", title="Quality Tracker", icon=":material/delete:")

pg = st.navigation([get_started_page, quality_tracker_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()