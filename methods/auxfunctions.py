import streamlit as st
from .recursos_eventos import Event
from datetime import date, datetime, time
#==========================|   CAMBIO DE VARIABLES GLOBALES PRINCIPALES   |========================================================================

def cambiar_pagina(nombre_pagina: str):
    st.session_state.pagina_actual = nombre_pagina
def agregar_evento(nuevo_evento: Event):
    st.session_state.events.append(nuevo_evento)
def agregar_fecha(fechas_evento: list[date]):
    for i in range(len(fechas_evento)):
        temporal = (fechas_evento[i],len(st.session_state.events)-1)
        st.session_state.dates.append(temporal)
    smart_dates_sorter(0,len(st.session_state.dates)-1,st.session_state.dates)

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
    if type(list[0])==tuple:
        merge2(l,m,r,list)
    else:
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

def merge2(l:int,m:int,r:int,list:list[date]):
    result = []
    l1, l2 = l, m+1
    while l1 <= m and l2 <= r:
        if list[l1][0] < list[l2][0]:
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


#------------------|   BUSQUEDA DE COINCIDENCIAS DE FECHAS EN EVENTOS   |-----------------------------------------------------------

def binary_search(left: int, right: int, list: list[tuple[date,int]], element: date):
    st.write(list)                                                                                             #########
    st.write(element)                                                                                        ###########
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
    if indexes[0] == -1:
        return False
    st.write(f"PRimer indice {indexes[0]}")                                                                        ########
    st.write(f"Ultimo indice {indexes[1]}")                                                                          ########
    for i in range(indexes[0],indexes[1]+1):
        main_indexes.append(list[i][1])
    return main_indexes

def binary_search_first(left: int, right: int, list: list[tuple[date,int]], element: date):
    if left > right or (left == right and (right == len(list)-1 or list[right+1][0] != element)):
        return -1
    middle = (left+right)//2
    if list[middle][0] != element and list[middle+1][0] == element:
        return middle+1
    elif list[middle][0] >= element:
        return binary_search_first(left, middle, list, element)
    else:
        return binary_search_first(middle+1,right,list,element)
    
def binary_search_last(left: int, right: int, list: list[tuple[date,int]], element: date):
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

def hours_collition(second_event_time: tuple[time], main_event_time: tuple[time]):
    se = second_event_time
    me = main_event_time
    if me[0] >= se[1] or me[1] <= se[0]:
        return False
    return True

def manage_resources(total_resources: dict[int], event_resources:dict[int]):
    for k in event_resources.keys():
        total_resources[k] -= event_resources[k]

def resource_collition(total_resources: dict[int], event_resources: dict[int]):
    collition = False
    st.write(total_resources)                                                                                     ##########
    for k in event_resources.keys():
        total_resources[k] -= event_resources[k]
        if total_resources[k] < 0:
            collition = True
    st.write(total_resources)                                                                                      ##########
    
    return collition
def collition_search(event,resources):
    collitions_result = []
    if st.session_state.dates:
        for i in range(len(event.date)):
            total_resources = resources
            avaliable_place = True
            values_list = binary_search(0,len(st.session_state.dates)-1,st.session_state.dates, event.date[i])
            st.write(values_list)                                                                                  #########
            if values_list:   
                for j in range(len(values_list)):
                    st.write(st.session_state.events[values_list[j]].time)                                         #########
                    st.write(hours_collition(st.session_state.events[values_list[j]].time, event.time))            #######
                    if hours_collition(st.session_state.events[values_list[j]].time, event.time):
                        manage_resources(total_resources,st.session_state.events[values_list[j]].resources)
                        if st.session_state.events[values_list[j]].place == event.place:
                            avaliable_place = False
                if resource_collition(total_resources,event.resources):
                    
                    collitions_result.append((event.date[i],total_resources,avaliable_place))
                elif not avaliable_place:
                    collitions_result.append((event.date[i],-1, False))            
        return collitions_result
    else:
        return collitions_result

def decoding_collitions(collitions, event):
    decoded = ""
    for dates in collitions:
        sentence = f"{dates[0]}: <br>"
        text = ""
        if dates[1] != -1:
            for k,v in dates[1].items():
                if v < 0:
                    text += f"{k}: {v*-1} faltantes  <br>"
        sentence += f"{text}"
        if not dates[2]:
            sentence += f"{event.place} no disponible <br>"
        decoded += f"{sentence}  <br>"
    return decoded



#==============|   BUSQUEDA DE PROXIMO INTERVAlO DISPONIBLE   |===================================================================
def weekdays_search(event):
    weekdays = []
    for x in event.dates:
        if x.weekday() not in validation:
            validation.append(x.weekday)
    validation = [0,0,0,0,0,0,0]
    for x in weekdays:
        validation[x] = 1
    return validation
def frecuency_type(event):
    rest = event.dates[-1] - event.dates[0]
    if len(event.dates) == 1:
        return 0 
    elif rest.days%7==0:
        return 1
    elif rest.days%28==0 or rest.days%29==0 or rest.days%30==0 or rest.days%31==0:
        return 2
    else:
        pass

    
    
def next_gap():
    return "Hola"