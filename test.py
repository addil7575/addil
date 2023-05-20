# simple app to test stremlit
import streamlit as st
st.title("hello word")
st.header("this hearder")
st.subheader("this is a subheader")
st.write("simple test for streamlit")
if st.button("click me") :
    st.write(" you clicked me")
    st.balloons()
st.sidebar.header("this is a sidebar")    
# create a button in the sidebar
button = st.sidebar.button(label="press me please")
if button : 
    st.sidebar.write("hello there")
    st.sidebar.balloons()
# create 2 columns(2)
col1,col2 =st.columns(2)
col1.header("this is column1") 
col1.write("this is column1")
col2.header("this is column2")
col2.write("this is column2")
# add a selectbox('selectionnez une option',('email','home phone','mobile phone'))
option = st.selectbox('Selectionnez une option',('email','home phone','mobile phone'))
st.write('you select',option)
