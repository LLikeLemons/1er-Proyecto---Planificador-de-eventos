import streamlit as st
from recursos_eventos import Event
from datetime import date, datetime, time
#==========================|   CAMBIO DE VARIABLES GLOBALES PRINCIPALES   |========================================================================

def cambiar_pagina(nombre_pagina: str):
    st.session_state.pagina_actual = nombre_pagina
def agregar_evento(nuevo_evento: Event):
    st.session_state.eventos.append(nuevo_evento)
def agregar_fecha(fechas_evento: list[tuple[date,int]]):
    st.session_state.dates.append((fechas_evento,len(st.session_state.events)))
    smart_dates_sorter(st.session_state.dates)

#==================================================================================================================================================

def opciones_salida(new_event):
    col1, col2 = st.columns(2,width=270,border=True)
    with col1:
        if st.button("Cancelar",use_container_width=True):
            cambiar_pagina("inicio")
    with col2:
        if st.button("Confirmar",use_container_width=True):
            agregar_evento(new_event)
            cambiar_pagina("inicio")

#======================|   ORDENADOR DE FECHAS   |=================================================================================================

def smart_dates_sorter(l:int,r:int,list:list[date]):
    if l>=r: return
    m = (l+r)//2
    smart_dates_sorter(l,m,list)
    smart_dates_sorter(m+1,r,list)
    merge(l,m,r,list)

def merge(l:int,m:int,r:int,list:list[date]):
    result = []
    l1, l2 = l, m+1
    while l1 <= m and l2 <= r:
        if list[l1] < list[l2]:
            result.append(list[l1])
            l1+=1
        else:
            result.append(list[l2])
            l2+=1
    result.extend(list[l1:m+1])
    result.extend(list[l2:r+1])
    for i in range(len(result)):
        list[l+i] = result[i]

#======================|   BUSQUEDA DE COLISIONES DE RECURSOS Y HORARIOS EN EVENTOS   |=======================================================


#------------------|   BUSQUEDA DE OCURRENCIAS DE FECHAS EN EVENTOS   |-----------------------------------------------------------

def binary_search(left, right, list, element):
    indexes = [0,0]
    main_indexes = []
    if list[0][0] == element:
        indexes[0] = 0
    else:
        indexes[0] = binary_search_first(left, right, list, element)
    if list[len(list)-1][0] == element:
        indexes[1] = len(list)-1
    else:
        indexes[1] = binary_search_last(left, right, list, element)
    for i in range(indexes[0],indexes[1]):
        main_indexes.append(list[i][1])
    return main_indexes

def binary_search_first(left,right,list,element):
    if left > right or (left == right and (right == len(list)-1 or list[right+1][0] != element)):
        return -1
    middle = (left+right)//2
    if list[middle][0] != element and list[middle+1][0] == element:
        return middle+1
    elif list[middle][0] >= element:
        return binary_search_first(left, middle, list, element)
    else:
        return binary_search_first(middle+1,right,list,element)
    
def binary_search_last(left,right,list,element):
    if left > right or (left == right and list[right-1][0] != element):
        return -1
    middle = (left+right)//2
    if list[middle][0] != element and list[middle-1][0] == element:
        return middle-1
    elif list[middle][0] <= element:
        return binary_search_last(middle+1, right, list, element)
    else:
        return binary_search_last(left,middle,list,element)

#-------------------------------------------------------------------------------------------------------------------------------

def hours_collition(second_event_time: time, main_event_time: time):
    se = second_event_time, me = main_event_time
    if me[0] >= se[1] or me[1] <= se[0]:
        return False
    return True

def manage_resources(total_resources: dict[int], event_resources:dict[int]):
    for k in event_resources.keys():
        total_resources[k] -= event_resources[k]


def collition_search(event):
    collitions_result = []
    
    for i in range(len(event.date)):
        total_resources = st.session_state.resources
        avaliable_place = True
        values_list = binary_search(st.session_state.dates, event.date[i])        
        if values_list:   
            for j in range(len(values_list)):
                if hours_collition(st.session_state.events[values_list[j]].hours, event.hour):
                    manage_resources(total_resources,st.session_state.events[values_list[j]].resources)
                    if st.session_state.events[values_list[j]].place == event.place:
                        avaliable_place = False
        collitions_result.append((total_resources,avaliable_place))

#==================================================================================================================================================
