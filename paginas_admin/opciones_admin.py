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
                #cambiar_pagina("Manejo de Helicoptero")
                manejo_helicoptero(True,event)
            elif type == "Capacitación de Instructores":
                #cambiar_pagina("Capacitacion de Instructores")
                capacitacion_intructor(True,event)
            elif type == "Capacitación SWAT":
                #cambiar_pagina("Capacitacion SWAT")
                capacitacion_swat(True,event)
            elif type == "Práctica de Tiro":
                #cambiar_pagina("Practica de Tiro")
                practica_tiro(True,event)
            elif type == "Práctica de Conducción":
                #cambiar_pagina("Practica de Conduccion")
                practica_conduccion(True,event)
            elif type == "Entrenamiento Físico":
                #cambiar_pagina("Entrenamiento Fisico")
                entrenamiento_fisico(True,event)
            elif type == "Persecución y aprehensión vehicular":
                #cambiar_pagina("Persecución y aprehensión vehicular")
                persecusion_vehiculo(True,event)
            elif type == "Intervención a Domicilio":
                #cambiar_pagina("Intervención a Domicilio")
                intervencion_domicilio(True,event)
            else:
                #cambiar_pagina("Simulacros con Rehenes")
                simulacro_rehenes(True,event)
           
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
        elif st.session_state.dates[i][1] == index:
            del st.session_state.dates[i]

#===========|   PARA LOS RECURSOS   |============================

def collition_search2(date,time,resources):
    total_places = []
    if st.session_state.dates:        
        total_resources = deepcopy(resources)
        values_list = binary_search(0,len(st.session_state.dates)-1,st.session_state.dates, date)
        if values_list:   
            for j in range(len(values_list)):  
                if hours_collition(st.session_state.events[values_list[j]].time, time):
                    manage_resources(total_resources,st.session_state.events[values_list[j]].resources)
                    if st.session_state.events[values_list[j]].place in total_places:
                        total_places -= st.session_state.events[values_list[j]].place
    return total_resources, total_places
