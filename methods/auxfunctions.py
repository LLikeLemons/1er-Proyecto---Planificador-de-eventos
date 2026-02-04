import streamlit as st
from methods.recursos_eventos import Event
from methods.recalibrate import recalibrate_dates_index
from datetime import date, datetime, time, timedelta
from copy import deepcopy
#==========================|   CAMBIO DE VARIABLES GLOBALES PRINCIPALES   |=============================================================================================

def cambiar_pagina(nombre_pagina: str):
    st.session_state.pagina_actual = nombre_pagina
def agregar_evento(nuevo_evento: Event):
    st.session_state.events.append(nuevo_evento)
def agregar_fecha(fechas_evento: list[date]):
    for i in range(len(fechas_evento)):
        temporal = (fechas_evento[i],len(st.session_state.events)-1)
        st.session_state.dates.append(temporal)
    smart_dates_sorter(0,len(st.session_state.dates)-1,st.session_state.dates)


#======================|   ORDENADOR DE FECHAS   |======================================================================================================================

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



#======================|   BUSQUEDA DE COLISIONES DE RECURSOS Y HORARIOS EN EVENTOS   |=================================================================================


#------------------|   BUSQUEDA DE COINCIDENCIAS DE FECHAS EN EVENTOS   |-----------------------------------------------------------------------------------------------

def binary_search(left: int, right: int, list: list[tuple[date,int]], element: date):
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

#-----------|   FUNCIONES AUXILIARES DE COLLITION_SEARCH   |------------------------------------------------------------------------------------------------------------

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
    for k in event_resources.keys():
        total_resources[k] -= event_resources[k]
        if total_resources[k] < 0:
            collition = True   
    return collition

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def collition_search(event,resources,looking_gap=False,date_gap=None,editor=False,editable_event=None,index=None):
    if editor:
        program_predates = deepcopy(st.session_state.dates)
        program_dates = []
        program_dates = recalibrate_dates_index(index,program_predates)
        

        program_preevents = deepcopy(st.session_state.events)
        program_events = []
        for i in range(len(program_preevents)):
            if i != index:
                program_events.append(program_preevents[i])

    else:
        program_dates = st.session_state.dates
        program_events = st.session_state.events
    collitions_result = []
    if not looking_gap:
        date_input = event.date
    else:
        date_input = date_gap
    if program_dates:
        for i in range(len(date_input)):
            total_resources = deepcopy(resources)
            avaliable_place = True
            values_list = binary_search(0,len(program_dates)-1,program_dates, date_input[i])
            if values_list:   
                for j in range(len(values_list)):
                    if hours_collition(program_events[values_list[j]].time, event.time):
                        manage_resources(total_resources,program_events[values_list[j]].resources)
                        if program_events[values_list[j]].place == event.place:
                            avaliable_place = False
                if resource_collition(total_resources,event.resources):
                    
                    collitions_result.append((date_input[i],total_resources,avaliable_place))
                elif not avaliable_place:
                    collitions_result.append((date_input[i],-1, False))            
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



#==============|   BUSQUEDA DE PROXIMO INTERVAlO DISPONIBLE   |=========================================================================================================
#----------------|   FUNCIONES AUXILIARES DE NEXT_GAP   |---------------------------------------------------------------------------------------------------------------
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

def range_addition(range_input):
    tuple_1 = range_input[0]
    date_input = []
    while tuple_1 < range_input[1]:
        if tuple_1.weekday() != 6:
            date_input.append(tuple_1)
        tuple_1 += timedelta(days=1)
    return date_input

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def next_gap(event,resources,editor=False,index=None):
#-------|  inicializo la variable firstdate   |--------------------------------------------------------------------------------------------------------------------------
    datetime0 = datetime.now()
    datetime1 = date(datetime0.year,datetime0.month,datetime0.day)
    timed = time(datetime0.hour,datetime0.minute)
    if event.frecuency_type == "Frecuencia mensual":
        first_date = event.date[0]
        datetime2 = date(datetime1.year,datetime1.month+1,datetime1.day)
        while datetime2 < first_date:
                first_date = date(first_date.year,first_date.month-1,first_date.day)  
    elif event.frecuency_type == "Frecuencia semanal":
        weekday = event.date[0].weekday()    
        first_date = event.date[0]
        datetime3 = datetime1 + timedelta(days=7)
        while datetime3 <= first_date:
                first_date -= timedelta(days=7)
    elif datetime1.weekday() != 6:
        first_date = datetime1  
    else:
        first_date = datetime1 + timedelta(days=1)       
        
#---------|   encuentra el tipo de requisito y la lista de fechas   |---------------------------------------------------------------------------------------------------
    while True: 
        date_input = []

        if event.frecuency_type == "Frecuencia mensual": 
            date_input = [first_date]                  
            next_date = first_date
            for i in range(event.frecuency):
                next_date = date(next_date.year,next_date.month+1,next_date.day)
                date_input.append(next_date)

        elif event.frecuency_type == "Rango de días":
            difference = event.date[-1] - event.date[0]
            st.write(difference)
            tuple_1 = (first_date,first_date+difference)
            date_input = range_addition(tuple_1)

        elif event.frecuency_type == "Frecuencia semanal":            
            attempts = event.week_days[:-1]
            next_date = first_date
            for i in range(len(attempts)):
                if attempts[i]:
                    next_date = first_date + timedelta(days=(i-weekday)%7)
                    date_input.append(next_date)
                    for j in range(event.frecuency):
                        next_date += timedelta(days=7)
                        date_input.append(next_date)
            
        else:
            date_input = [first_date]
#-------------|   busca la colision   |---------------------------------------------------------------------------------------------------------------------------------
        if not collition_search(event,resources,True,date_input,editor=editor,index=index):
            if first_date == datetime1:
                if event.time[0] > timed and event.time[1] > timed:
                    return first_date
            else:
                return first_date   
#-------------|   En caso negativo suma valores a la fecha   |----------------------------------------------------------------------------------------------------------
        if event.frecuency_type == "Frecuencia mensual":
            first_date = date(first_date.year,first_date.month+1,first_date.day)

        elif event.frecuency_type == "Frecuencia semanal":
            first_date+=timedelta(days=7)
            
        else:
            if first_date.weekday() != 6:
                first_date+=timedelta(days=1)  
            else:
                first_date+=timedelta(days=2)            
        

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////