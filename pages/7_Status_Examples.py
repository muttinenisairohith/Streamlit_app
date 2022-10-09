
"""
st.success(): This function is used to display a success message. 
st.error(): This function is used to display an error message. 
st.warnig(): This function is used to display a warning message. 
st.info(): This function is used to display an informational message. 
st.exception(): This function is used to display an exception message.
"""

import streamlit as st

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
