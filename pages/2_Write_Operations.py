
"""
st.title(): This function allows you to add the title of the app. 
st.header(): This function is used to set header of a section. 
st.markdown(): This function is used to set a markdown of a section. 
st.subheader(): This function is used to set sub-header of a section. 
st.caption(): This function is used to write caption. 
st.code(): This function is used to set a code. 
st.latex(): This function is used to display mathematical expressions formatted as LaTeX.
"""

import streamlit as st

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
