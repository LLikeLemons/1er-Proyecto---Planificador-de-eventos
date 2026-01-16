import streamlit as st
import time
from datetime import datetime
from auxfunctions import *
from P_C import practica_conduccion

def main():
    if "pagina_actual" not in st.session_state:
        st.session_state.pagina_actual = "inicio"
    if "eventos" not in st.session_state:
        st.session_state.events = []
    if "dates" not in st.session_state:
        st.session_state.dates = []
    if "resources" not in st.session_state:
        st.session_state.resources = {
    "AMP": 50,
    "Bicicletas": 30,
    "Blancos de práctica": 30,
    "Chalecos Antibalas":100,
    "Entrenadores de Defensa Personal":5,
    "Entrenadores Físicos":5,
    "Equipo Táctico":20,
    "Escopetas": 50,
    "Instructores": 30,
    "Instructores de unidades especiales":6,
    "Libro de capacitación para agentes I":50,
    "Libro de capacitación para agentes II":50,
    "Manuales de conducción para agentes": 50,
    "Moto Mary-Policía": 20,
    "Oficiales de alto rango": 7,
    "Proyectores": 10,
    "Vehículo Z4": 30,
    "Vehículo Interceptor": 5,
}
    st.set_page_config(layout="wide")
    
    if st.session_state.pagina_actual == "inicio":
        st.session_state.practica_conduccion = False

        with st.sidebar:
            st.header("MENU", divider="red")
            st.subheader("Cursos de Capacitación", divider="red")
            if st.button("Manejo de Helicóptero", use_container_width=True):
                cambiar_pagina("cursos_capacitación")
            if st.button("Capacitación de Instructores", use_container_width=True):
                cambiar_pagina("cursos_capacitación")
            if st.button("Capacitación SWAT", use_container_width=True):
                cambiar_pagina("cursos_capacitación")

            st.subheader("Entrenamientos", divider="red")
            if st.button("Prácticas de tiro", use_container_width=True):
                cambiar_pagina("entrenamientos")
            if st.button("Práctica de Conducción", use_container_width=True):
                cambiar_pagina("entrenamientos")
                st.session_state.practica_conduccion = True
            if st.button("Entrenamiento Fisico", use_container_width=True):
                cambiar_pagina("entrenamientos")

            st.subheader("Simulacros", divider="red")
            if st.button("Persecución y aprehensión vehicular", use_container_width=True):
                cambiar_pagina("Simulacros")
            if st.button("Intervención a Domicilio", use_container_width=True):
                cambiar_pagina("Simulacros")
            if st.button("Simulacros con Rehenes", use_container_width=True):
                cambiar_pagina("Simulacros")

            st.markdown("""<div 
                        style='
                        color: #000000;
                        border-bottom: 4px solid blue;'>
            </div>""",unsafe_allow_html=True)
            if st.button("Recursos", use_container_width=True):
                cambiar_pagina("recursos")


        st.markdown("""<div
                    style='
                    color: red;
                    font-size: 80px;
                    font-weight: bold;
                    text-align: center;'> PRUEBA DE PAGINA
        </div>""", unsafe_allow_html=True)
        
        
        # placeholder = st.empty()
        # while st.session_state.pagina_actual == "inicio":
        #     now = datetime.now()
        #     fecha_hora = now.strftime("%d/%m/%Y %H:%M:%S")
        #     with placeholder.container():
        #         st.metric("",fecha_hora, label_visibility="collapsed")

    if st.session_state.pagina_actual == "entrenamientos":
        if st.session_state.practica_conduccion:
            practica_conduccion()

    
if __name__ == "__main__":
    main()