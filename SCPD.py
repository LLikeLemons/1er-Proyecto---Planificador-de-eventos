import streamlit as st
from paginas_eventos import *
from methods import *
from paginas_admin import edicion, resources_search, edition_selector

def main():
#========|   CARGA DE DATOS INICIAL   |============================================================================================================
    storage = load_json("data.json")
    for i in range(len(storage[0])):
        storage[0][i] = dict_date_event(storage[0][i])
    if "pagina_actual" not in st.session_state:
        st.session_state.pagina_actual = "inicio"
    if "dates" not in st.session_state:
        st.session_state.dates = storage[0]
    if "eventos" not in st.session_state:
        st.session_state.events = dict_event(storage[1])

#===============|   PAGINA PRINCIPAL   |=========================================================================================================
    st.set_page_config(layout="wide")
    
    if st.session_state.pagina_actual == "inicio":
        tab1,tab2,tab3 = st.tabs(["INICIO", "RECURSOS", "EDICION"])
        with tab1:
            st.markdown("""<div style='
                border-bottom: 4px solid ;
                border-image: linear-gradient(130deg, black, darkblue) 1;
                font-size: 80px;
                text-align: center;
                text-weight: bold;
                '>PRUEBA DE PAGINA
                </div>""",unsafe_allow_html=True)
            st.text(st.session_state.dates)
            st.text(st.session_state.events)
        with tab2:
            resources_search()
        with tab3:
            edicion()
                


#========|   MENU DE OPCIONES DE EVENTOS EN LA SIDEBAR   |========================================================================================
    
        with st.sidebar:
            st.header("MENU", divider="red")
            st.subheader("Cursos de Capacitación", divider="red")
            st.button("Manejo de Helicóptero", use_container_width=True, on_click=lambda: cambiar_pagina("Manejo de Helicoptero"))                
            st.button("Capacitación de Instructores", use_container_width=True, on_click=lambda: cambiar_pagina("Capacitacion de Instructores"))               
            st.button("Capacitación SWAT", use_container_width=True, on_click=lambda: cambiar_pagina("Capacitacion SWAT"))                

            st.subheader("Entrenamientos", divider="red")
            st.button("Prácticas de Tiro", use_container_width=True,on_click=lambda: cambiar_pagina("Practica de Tiro"))                
            st.button("Práctica de Conducción", use_container_width=True, on_click=lambda: cambiar_pagina("Practica de Conduccion"))
            st.button("Entrenamiento Fisico", use_container_width=True,on_click=lambda: cambiar_pagina("Entrenamiento Fisico"))
                
            st.subheader("Simulacros", divider="red")
            st.button("Persecución y aprehensión vehicular", use_container_width=True,on_click=lambda: cambiar_pagina("Persecución y aprehensión vehicular"))                
            st.button("Intervención a Domicilio", use_container_width=True,on_click=lambda: cambiar_pagina("Intervención a Domicilio"))                
            st.button("Simulacros con Rehenes", use_container_width=True,on_click=lambda: cambiar_pagina("Simulacros con Rehenes"))

#===============|   CAMBIOS DE PAGINAS   |=========================================================================================================
    elif st.session_state.pagina_actual == "Manejo de Helicoptero":
        manejo_helicoptero()
    elif st.session_state.pagina_actual == "Capacitacion de Instructores":
        capacitacion_intructor()
    elif st.session_state.pagina_actual == "Capacitacion SWAT":
        capacitacion_swat()
    elif st.session_state.pagina_actual == "Practica de Tiro":
        practica_tiro()
    elif st.session_state.pagina_actual == "Practica de Conduccion":
        practica_conduccion()
    elif st.session_state.pagina_actual == "Entrenamiento Fisico":
        entrenamiento_fisico()
    elif st.session_state.pagina_actual == "Persecución y aprehensión vehicular":
        persecusion_vehiculo()
    elif st.session_state.pagina_actual == "Intervención a Domicilio":
        intervencion_domicilio()
    elif st.session_state.pagina_actual == "Simulacros con Rehenes":
        simulacro_rehenes()
    elif st.session_state.pagina_actual == "edicion":
        edition_selector(st.session_state.edition_values[0],
                         st.session_state.edition_values[1],
                         st.session_state.edition_values[2])
    
if __name__ == "__main__":
    main()