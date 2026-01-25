import streamlit as st
from pathlib import Path
from PIL import Image
from paginas_eventos import *
from methods import *
from paginas_admin import edicion, resources_search, edition_selector, visualizador_eventos

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
    st.set_page_config(layout="wide",page_title="AGENDA",page_icon="📑")

    if st.session_state.pagina_actual == "inicio":
        tab1,tab2,tab3,tab4 = st.tabs(["INICIO", "RECURSOS", "EDICIÓN","VISUALIZACIÓN"])
        with tab1:
            st.markdown("""<div style='
                border: 4px solid red;
                font-size: 30px;
                text-align: center;
                font-weight: bold;
                '>AGENDA DE EVENTOS DE LA POLICÍA
                </div>""",unsafe_allow_html=True)
            img_path = storage_path("logo.png")
            st.image(str(img_path), use_container_width=True)
            # st.text(st.session_state.dates)
            # st.text(st.session_state.events)
        with tab2:
            resources_search()
        with tab3:
            edicion()
        with tab4:
            visualizador_eventos()
                


#========|   MENU DE OPCIONES DE EVENTOS EN LA SIDEBAR   |========================================================================================
    
        with st.sidebar:
            st.header("MENÚ", divider="red",help="Menú de opciones de eventos a agregar a la agenda")
            st.subheader("Cursos de Capacitación", divider="red")
            st.button("Manejo de Helicóptero", use_container_width=True, on_click=lambda: cambiar_pagina("Manejo de Helicoptero"))                
            st.button("Capacitación de Instructores", use_container_width=True, on_click=lambda: cambiar_pagina("Capacitacion de Instructores"))               
            st.button("Capacitación SWAT", use_container_width=True, on_click=lambda: cambiar_pagina("Capacitacion SWAT"))                

            st.subheader("Entrenamientos", divider="red")
            st.button("Prácticas de Tiro", use_container_width=True,on_click=lambda: cambiar_pagina("Practica de Tiro"))                
            st.button("Práctica de Conducción", use_container_width=True, on_click=lambda: cambiar_pagina("Practica de Conduccion"))
            st.button("Entrenamiento Físico", use_container_width=True,on_click=lambda: cambiar_pagina("Entrenamiento Fisico"))
                
            st.subheader("Simulacros", divider="red",help="Los simulacros en lugares públicos requieren permiso previo del municipio")
            st.button("Persecución y aprehensión vehicular", use_container_width=True,on_click=lambda: cambiar_pagina("Persecucion y aprehension vehicular"))                
            st.button("Intervención a Domicilio", use_container_width=True,on_click=lambda: cambiar_pagina("Intervencion a Domicilio"))                


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
    elif st.session_state.pagina_actual == "Persecucion y aprehension vehicular":
        persecusion_vehiculo()
    elif st.session_state.pagina_actual == "Intervencion a Domicilio":
        intervencion_domicilio()
    elif st.session_state.pagina_actual == "edicion":
        edition_selector(st.session_state.edition_values[0],
                         st.session_state.edition_values[1],
                         st.session_state.edition_values[2])
if __name__ == "__main__":
    main()