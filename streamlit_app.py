import streamlit as st
st.logo("https://placehold.co/1000x150/transparent/grey?font=montserrat&text=•|•|•++M+H+C+C+Q+T",
    icon_image="https://placehold.co/1000x1000/transparent/grey?font=montserrat&text=•|•|•"
)

get_started_page = st.Page("pages/get_started.py", title="Get Started", icon=":material/rocket:")
quality_tracker_page = st.Page("pages/quality_tracker.py", title="Quality Tracker", icon=":material/dynamic_form:")
configuration_page = st.Page("pages/configuration.py",title="Configuration", icon=":material/build_circle:")
pg = st.navigation([get_started_page, quality_tracker_page, configuration_page])
st.set_page_config(page_title="MHCCQT", page_icon=":material/graphic_eq:")
pg.run()
