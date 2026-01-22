import streamlit as st
from paginas_eventos import *
def edition_selector(index: int,edit=False,eliminate=False,):
        if eliminate:
            del st.session_state.events[index]
            recalibrate_dates_index(index)
        else:
            event = st.session_state.events[index]
            type = st.session_state.events[index].type
            if type == "Manejo de Helicóptero":
                manejo_helicoptero(event)
            elif type == "Capacitación de Instructores":
                capacitacion_intructor(event)
            elif type == "Capacitación SWAT":
                capacitacion_swat(event)
            elif type == "Práctica de Tiro":
                practica_tiro(event)
            elif type == "Práctica de Conducción":
                practica_conduccion(event)
            elif type == "Entrenamiento Físico":
                entrenamiento_fisico(event)
            elif type == "Persecución y aprehensión vehicular":
                persecusion_vehiculo(event)
            elif type == "Intervención a Domicilio":
                intervencion_domicilio(event)
            else:
                simulacro_rehenes(event)

def week_days_decoding(list: list[int]):
    frecuency = ""
    for i in range(len(list)):
        if list[i]:
            if i == 0:
                frecuency += "Lunes -"
            elif i == 1:
                frecuency += "Martes - "
            elif i == 2:
                frecuency += "Miercoles - "
            elif i == 3:
                frecuency += "Jueves - "
            elif i == 4:
                frecuency += "Viernes - "
            else:
                frecuency += "Sabado - "
   
    frecuency = frecuency.strip(" - ")

    return frecuency

def recalibrate_dates_index(index):
    for i in range(len(st.session_state.dates)):
        if st.session_state.dates[i][1] > index:
            st.session_state.dates[i][1] -= 1