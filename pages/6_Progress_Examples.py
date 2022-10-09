
"""
st.balloons(): This function is used to display balloons for celebration. 
st.progress(): This function is used to display a progress bar. 
st.spinner(): This function is used to display a temporary waiting message during execution.
"""

import streamlit as st
import time

st.balloons()
st.progress(90)
with st.spinner('Wait for it...'):
    time.sleep(10)
