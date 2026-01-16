import streamlit as st
def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_actual = nombre_pagina
def agregar_evento(nuevo_evento):
    st.session_state.eventos.append(nuevo_evento)


def opciones_salida(new_event):
    col1, col2 = st.columns(2,width=270,border=True)
    with col1:
        if st.button("Cancelar",use_container_width=True):
            cambiar_pagina("inicio")
    with col2:
        if st.button("Confirmar",use_container_width=True):
            agregar_evento(new_event)
            cambiar_pagina("inicio")

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

def collition_search(list):
    pass

