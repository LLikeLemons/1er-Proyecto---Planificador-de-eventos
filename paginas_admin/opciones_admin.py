import streamlit as st
from paginas_eventos import *
def edition_selector(index: int,edit=False,eliminate=False,):
        if eliminate:
            st.session_state.events.remove[index]
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