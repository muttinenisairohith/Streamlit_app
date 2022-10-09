
"""
st.checkbox(): This function returns a Boolean value. When the box is checked, it returns a True value, otherwise a False value. 
st.button(): This function is used to display a button widget. 
st.radio(): This function is used to display a radio button widget. 
st.selectbox(): This function is used to display a select widget. 
st.multiselect(): This function is used to display a multiselect widget. 
st.select_slider(): This function is used to display a select slider widget. 
st.slider(): This function is used to display a slider widget.
"""

import streamlit as st

checkbox = st.checkbox('yes')
radio = st.radio('Pick your gender',['Male','Female'])
selectbox = st.selectbox('Pick your gender',['Male','Female'])
mutliselect = st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
select_slider = st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
slider = st.slider('Pick a number', 0,50)
button = st.button('Submit')

#button handler
if(button):
    st.write("Checbox value : ", checkbox)
    st.write("radio value : ", radio)
    st.write("selectbox value : ", selectbox)
    st.write("mutliselect value : ", mutliselect)
    st.write("select_slider value : ", select_slider)
    st.write("slider value : ", slider)
    #print("Button is clicked")
