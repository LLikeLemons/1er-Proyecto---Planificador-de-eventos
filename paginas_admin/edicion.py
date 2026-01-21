import streamlit as st
from methods import *
from datetime import datetime, date, time, timedelta
from .opciones_admin import *

def edicion():
    containter = st.container(border=True)
    options = []
    captions = []
    x = 4
    for i in range(len(st.session_state.events)):
        options.append(f"EVENTO No{i+1}: {st.session_state.events[i].type}")
        if st.session_state.events[i].schedule == "Frecuencia semanal":
            captions.append(f"""Primera fecha: {st.session_state.events[i].dates[0]} ||
                        Tipo de Horario: Frecuencia semanal || 
                        Repeticiones: {x} semanas || 
                        Días de la semana: {x}""")
        elif st.session_state.events[i].schedule == "Frecuencia mensual":
            captions.append(f"""Primera fecha: {st.session_state.events[i].dates[0]} ||
                        Tipo de Horario: Frecuencia mensual || 
                        Repeticiones: {x} meses""")
        elif st.session_state.events[i].schedule == "Rango de días":
            captions.append(f"""Primera fecha: {st.session_state.events[i].dates[0]} ||
                            Última fecha: {st.session_state.events[i].dates[-1]} || 
                            Tipo de Horario: Rango de días """)
        else:
            captions.append(f"""Fecha: {st.session_state.events[i].dates[0]} ||
                        Tipo de Horario: Evento único""")
    selection = st.radio(
        options=options,
        captions=captions
    )

    with containter:
        col1,col2 = st.columns(2)    
        if selection == None:
            st.header("Seleccione un Evento")
        else:
            index = options.index(selection)
            col1.button(label="Editar",on_click=edition_selector(index,edit=True),type="tertiary",)
            col2.button(label="Eliminar",on_click=edition_selector(index,eliminate=True))

