import streamlit as st

col1, col2 = st.columns(2,border=True)
tab1, tab2 = col1.tabs(["Hola","adios"])
with tab1:
    st.text_area("go")
with tab2:
    st.text_area("went")

with col2:
    st.text_area("hola")    