
"""
st.number_input(): This function is used to display a numeric input widget. 
st.text_input(): This function is used to display a text input widget. 
st.date_input(): This function is used to display a date input widget to choose a date. 
st.time_input(): This function is used to display a time input widget to choose a time. 
st.text_area(): This function is used to display a text input widget with more than a line text. 
st.file_uploader(): This function is used to display a file uploader widget. 
st.color_picker(): This function is used to display color picker widget to choose a color.
"""

import streamlit as st

number_input = st.number_input('Pick a number', 0,10)
text_input = st.text_input('Email address')
date_input = st.date_input('Travelling date')
time_input = st.time_input('School time')
text_area = st.text_area('Description')
file_uploader = st.file_uploader('Upload a photo')
color_picker = st.color_picker('Choose your favorite color')
button = st.button('Submit')

#Button Handler
if(button):
    st.write(number_input)
    st.write(text_input)
    st.write(date_input)
    st.write(time_input)
    st.write(text_area)
    st.write(file_uploader)
    st.write(color_picker)
