import streamlit as st
from datetime import date, datetime, time

# col1, col2 = st.columns(2,border=True)
# tab1, tab2 = col1.tabs(["Hola","adios"])
# with tab1:
#     st.text_area("go")
# with tab2:
#     st.text_area("went")

# with col2:
#     st.text_area("hola")    

date1 = time(9,25,1)
date2 = time(8,25,10)

if date1 <= date2:
    print("Si")
else:
    print("No")