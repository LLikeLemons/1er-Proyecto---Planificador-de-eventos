import streamlit as st
from paginas_eventos import *
from methods import recalibrate_dates_index, cambiar_pagina
#========|   PARA LA PAGINA DE EDICION   |========================================================================================================
def edition_selector(index: int,edit=False,eliminate=False,):
        
        if eliminate:
            del st.session_state.events[index]
            st.session_state.dates = recalibrate_dates_index(index,st.session_state.dates)            
            dict_dates = deepcopy(st.session_state.dates)
            for i in range(len(dict_dates)):
                dict_dates[i] = date_event_dict(dict_dates[i])
            dict_events = deepcopy(st.session_state.events)
            for i in range(len(dict_events)):
                dict_events[i] = dict_events[i].to_dict()        
            storage = [dict_dates,dict_events]
            save_json(storage,"data.json")
            return
        else:
            event = st.session_state.events[index]
            type = st.session_state.events[index].type
            
            if type == "Manejo de Helicóptero":
                #cambiar_pagina("Manejo de Helicoptero")
                manejo_helicoptero(True,event,index)
            elif type == "Capacitación de Instructores":
                #cambiar_pagina("Capacitacion de Instructores")
                capacitacion_intructor(True,event,index)
            elif type == "Capacitación SWAT":
                #cambiar_pagina("Capacitacion SWAT")
                capacitacion_swat(True,event,index)
            elif type == "Práctica de Tiro":
                #cambiar_pagina("Practica de Tiro")
                practica_tiro(True,event,index)
            elif type == "Práctica de Conducción":
                #cambiar_pagina("Practica de Conduccion")
                practica_conduccion(True,event,index)
            elif type == "Entrenamiento Físico":
                #cambiar_pagina("Entrenamiento Fisico")
                entrenamiento_fisico(True,event,index)
            elif type == "Persecución y aprehensión vehicular":
                #cambiar_pagina("Persecución y aprehensión vehicular")
                persecusion_vehiculo(True,event,index)
            elif type == "Intervención a Domicilio":
                #cambiar_pagina("Intervención a Domicilio")
                intervencion_domicilio(True,event,index)
            else:
                #cambiar_pagina("Simulacros con Rehenes")
                simulacro_rehenes(True,event,index)
           
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



#===========|   PARA LOS RECURSOS   |=============================================================================================================

def collition_search2(date,time,resources):
    total_places = ["Academia Policial","Centro de entrenamiento","Pista de automovilismo"]
    total_resources = deepcopy(resources)
    if st.session_state.dates:        
        
        values_list = binary_search(0,len(st.session_state.dates)-1,st.session_state.dates, date)
        st.write(values_list)
        if values_list:   
            for j in range(len(values_list)):  
                if hours_collition(st.session_state.events[values_list[j]].time, time):
                    manage_resources(total_resources,st.session_state.events[values_list[j]].resources)
                    if st.session_state.events[values_list[j]].place in total_places:
                        total_places.remove(st.session_state.events[values_list[j]].place)
    return total_resources, total_places
