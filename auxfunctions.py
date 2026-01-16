import streamlit as st
from recursos_eventos import Event
#================================================================================================================================

def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_actual = nombre_pagina
def agregar_evento(nuevo_evento):
    st.session_state.eventos.append(nuevo_evento)
def agregar_fecha(fechas_evento):
    st.session_state.dates.append((fechas_evento,len(st.session_state.events)))
    smart_dates_sorter(st.session_state.dates)

#================================================================================================================================

def opciones_salida(new_event):
    col1, col2 = st.columns(2,width=270,border=True)
    with col1:
        if st.button("Cancelar",use_container_width=True):
            cambiar_pagina("inicio")
    with col2:
        if st.button("Confirmar",use_container_width=True):
            agregar_evento(new_event)
            cambiar_pagina("inicio")

#================================================================================================================================

def smart_dates_sorter(l,r,list):
    if l>=r: return
    m = (l+r)//2
    smart_dates_sorter(l,m,list)
    smart_dates_sorter(m+1,r,list)
    merge(l,m,r,list)

def merge(l,m,r,list):
    result = []
    l1, l2 = l, m+1
    while l1 <= m and l2 <= r:
        if dates_comparison(list[l1],list[l2]):
            result.append(list[l1])
            l1+=1
        else:
            result.append(list[l2])
            l2+=1
    result.extend(list[l1:m+1])
    result.extend(list[l2:r+1])
    for i in range(len(result)):
        list[l+i] = result[i]

def dates_comparison(date1,date2):
    if date1.year == date2.year:
        if date1.month == date2.month:
            if date1.day <= date2.day:
                return True
            return False
        elif date1.month < date2.month:
            return True
        return False
    elif date1.year < date2.year:
        return True
    return False
def hours_collition(event:Event):
    pass
def binary_search():
    pass
def resources_math():
    pass
def manage_resources():
    pass
def collition_search(event):
    collitions_result = []
    for i in range(len(list)):
        if hours_collition(event):
            for j in range(len(event.date)):
                if binary_search():
                    collition = resources_math()
                    collitions_result.append(collition)

def collition_search(event):
    collitions_result = []
    
    for i in range(len(event.date)):
        total_resources = []
        values_list = binary_search(st.session_state.dates, event.date[i])
        if values_list:            
            for j in range(len(values_list)):
                if hours_collition(st.session_state.events[values_list[j]].hours, event.hour):
                    total_resources = manage_resources(total_resources,st.session_state.events[values_list[j]].resources)
        collitions_result.append(total_resources)

                    
                    
