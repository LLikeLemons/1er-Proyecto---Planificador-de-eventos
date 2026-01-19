import streamlit as st
import time
from datetime import datetime
from auxfunctions import *
from auxfunctions_2 import *
from P_C import practica_conduccion
from recursos_eventos import *
def main():
    storage = load_json("data.json")
    for i in range(len(storage[0])):
        storage[0][i] = dict_date_event(storage[0][i])
    if "pagina_actual" not in st.session_state:
        st.session_state.pagina_actual = "inicio"
    if "dates" not in st.session_state:
        st.session_state.dates = storage[0]
    if "eventos" not in st.session_state:
        st.session_state.events = dict_event(storage[1])
    
    st.set_page_config(layout="wide")
    
    if st.session_state.pagina_actual == "inicio":

        with st.sidebar:
            st.header("MENU", divider="red")
            st.subheader("Cursos de Capacitación", divider="red")
            st.button("Manejo de Helicóptero", use_container_width=True, on_click=cambiar_pagina("manejo heli"))                
            st.button("Capacitación de Instructores", use_container_width=True, on_click=cambiar_pagina("instructores"))               
            st.button("Capacitación SWAT", use_container_width=True, on_click=cambiar_pagina("swat"))                

            st.subheader("Entrenamientos", divider="red")
            st.button("Prácticas de tiro", use_container_width=True,on_click=cambiar_pagina("practica de tiro"))                
            st.button("Práctica de Conducción", use_container_width=True,on_click=cambiar_pagina("practica conduccion"))
            st.button("Entrenamiento Fisico", use_container_width=True,on_click=cambiar_pagina("entrenamiento fisico"))
                
            st.subheader("Simulacros", divider="red")
            st.button("Persecución y aprehensión vehicular", use_container_width=True,on_click=cambiar_pagina("persecusion"))                
            st.button("Intervención a Domicilio", use_container_width=True,on_click=cambiar_pagina("intervencion"))                
            st.button("Simulacros con Rehenes", use_container_width=True,on_click=cambiar_pagina("rehenes"))
                        
            st.markdown("""<div 
                        style='
                        color: #000000;
                        border-bottom: 4px solid blue;'>
            </div>""",unsafe_allow_html=True)
            st.button("Recursos", use_container_width=True, on_click=cambiar_pagina("recursos"))
                


        st.markdown("""<div
                    style='
                    color: red;
                    font-size: 80px;
                    font-weight: bold;
                    text-align: center;'> PRUEBA DE PAGINA
        </div>""", unsafe_allow_html=True)
        st.text(st.session_state.dates)
        st.text(st.session_state.events)
    
    # pages = {
    #     "manejo heli":0,
    #     "swat":0,
    #     "instructores":0,
    #     "practica tiro":0,
    #     "practica_conduccion":practica_conduccion(),
    #     "entrenamiento fisico":0,
    #     "persecucion":0,
    #     "intervencion":0,
    #     "rehenes":0
    # }
    # pages[st.session_state.pagina_actual]
    
    # if st.session_state.pagina_actual == "practica conduccion":
    #     practica_conduccion()

    
if __name__ == "__main__":
    main()