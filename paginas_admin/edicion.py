import streamlit as st
from methods import *
from datetime import datetime, date, time, timedelta
from .opciones_admin import *

def edicion():
    containter = st.container(horizontal_alignment="center",vertical_alignment="top", horizontal=True,height="stretch")
    st.markdown("""<div style='border-top: 8px solid red'></div>""",unsafe_allow_html=True)
    options = []
    captions = []
    for i in range(len(st.session_state.events)):
        options.append(f"EVENTO No{i+1}: {st.session_state.events[i].type}")
        if st.session_state.events[i].frecuency_type == "Frecuencia semanal":
            captions.append(f"""Primera fecha: {st.session_state.events[i].date[0]} || 
                        Horario: {st.session_state.events[i].time[0]} - {st.session_state.events[i].time[1]} || 
                        Tipo de Frecuencia: Frecuencia semanal || 
                        Repeticiones: {st.session_state.events[i].frecuency} semanas || 
                        Días de la semana: {week_days_decoding(st.session_state.events[i].week_days)}""")
        elif st.session_state.events[i].frecuency_type == "Frecuencia mensual":
            captions.append(f"""Primera fecha: {st.session_state.events[i].date[0]} || 
                        Horario: {st.session_state.events[i].time[0]} - {st.session_state.events[i].time[1]} || 
                        Tipo de Frecuencia: Frecuencia mensual || 
                        Repeticiones: {st.session_state.events[i].frecuency} meses""")
        elif st.session_state.events[i].frecuency_type == "Rango de días":
            captions.append(f"""Primera fecha: {st.session_state.events[i].date[0]} || 
                            Horario: {st.session_state.events[i].time[0]} - {st.session_state.events[i].time[1]} || 
                            Última fecha: {st.session_state.events[i].date[-1]} || 
                            Tipo de Frecuencia: Rango de días """)
        else:
            captions.append(f"""Fecha: {st.session_state.events[i].date[0]} || 
                        Horario: {st.session_state.events[i].time[0]} - {st.session_state.events[i].time[1]} || 
                        Tipo de Frecuencia: Evento único""")
    selection = st.radio(
        "IS THIS GONNA WORK?????????????????????????????",
        options=options,
        captions=captions,
        label_visibility="collapsed",
        index=None
    )

    with containter:
        col1,col2 = st.columns(2)    
        if selection == None:
            containter.title("SELECCIONE UN EVENTO     ")
        else:
            st.session_state.index = options.index(selection)
            col1.button(label="Editar",type="primary",width="stretch")
            col2.button(label="Eliminar",width="stretch")


