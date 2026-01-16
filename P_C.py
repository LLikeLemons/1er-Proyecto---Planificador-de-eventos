import streamlit as st
from recursos_eventos import Event
from auxfunctions import *
from datetime import datetime, date, time, timedelta

def practica_conduccion():
    col0, col1 = st.columns([0.85,0.15], vertical_alignment="center")
    col2, col3 = st.columns([0.85,0.15], vertical_alignment="center")
    col4, col5  = st.columns([0.85,0.15], vertical_alignment="center")
    col6, col7, col8 = st.columns([0.25,0.25,0.5],border=True)
    date_validation = True
    
    st.set_page_config(layout="wide")
    col0.header("PLANIFICACIÓN DE EVENTO",divider="red")
    col2.subheader("Entrenamientos: Práctica de Conducción", divider="red")
    inst = 0
    with col4:
        repeticion = st.radio("Tipo de Horario y Repetición",
                    ["Evento único", "Repetición semanal", "Repetición mensual", "Rango de días"],
                    index=0, width="stretch", horizontal=True)
    
    cono = col6.number_input("Cantidad de conos", value=0, min_value=0)
    inst = col6.number_input("Cantidad de Instructores", value=0, min_value=0,help="Debe haber al menos un instructor por vehiculo" \
        " interceptor")
    with col7:        
        z4 = st.number_input("Cantidad de vehiculos Z4",value=0, min_value=0)
        inter = st.number_input("Cantidad de vehiculos Interceptor", value=inst, min_value=inst,)
        mary = st.number_input("Cantidad de motos Mary-Policia", value=0, min_value=0)
    with col6:
        
        option = ["Pista de automovilismo", "Centro de entrenamiento", "Academia Policial"]
        if inter > 0:
            option = [option[0]]
        place = st.selectbox("Lugar de practica", option,
                     help="Por cuestiones de seguridad los vehiculos Interceptor solo tienen permitido manejarse \n" \
                     "en la pista de automovilismo")
    
    
    if repeticion == "Evento único":
        date_input = col8.date_input("Fecha", value="today", min_value="today")
        time_input = col8.time_input("Hora de inicio")
        time_input = col8.time_input("Hora de conclusión")

    elif repeticion == "Rango de días":
        date_input = col8.date_input("Rango de fechas", value=["today","today"], min_value="today")
        time_input = col8.time_input("Hora de inicio")
        time_input = col8.time_input("Hora de conclusión")
        

    elif repeticion == "Repetición semanal":
        col9, col10 = col8.columns([0.3,0.7])
        prechecks = [0,0,0,0,0,0,0]
        validations = [0,0,0,0,0,0,0]
        first_date = col10.date_input("Fecha inicial", value="today", min_value="today")
        time_input = col10.time_input("Hora de inicio",value="now")
        time_input = col10.time_input("Hora de conclusión",value="now")

        weekday = first_date.weekday()
        for i in range(7):
            if i == weekday:
                prechecks[i] = True
                validations[i] = True
        
        with col9:
            Mo = st.checkbox("Lunes", prechecks[0], disabled=validations[0])
            Tu = st.checkbox("Martes", prechecks[1], disabled=validations[1])
            We = st.checkbox("Miercoles", prechecks[2], disabled=validations[2])
            Th = st.checkbox("Jueves", prechecks[3], disabled=validations[3])
            Fr = st.checkbox("Viernes", prechecks[4], disabled=validations[4])
            Sa = st.checkbox("Sabado", prechecks[5], disabled=validations[5])
        weeks = col5.slider("Cantidad de semanas", max_value=8)
        attempts = [Mo,Tu,We,Th,Fr,Sa]
        date_input = []
        next_date = first_date
        for i in range(len(attempts)):
            if attempts[i]:
                next_date = first_date + timedelta(days=(i-weekday)%7)
                date_input.append(next_date)
                st.text(i-weekday)
                for j in range(weeks):
                    next_date += timedelta(days=7)
                    date_input.append(next_date)
        st.text(date_input)

    elif repeticion == "Repetición mensual":            
        first_date = col8.date_input("Fecha inicial", value="today", min_value="today")
        time_input = col8.time_input("Hora de inicio")
        time_input = col8.time_input("Hora de conclusión")        
        months = col5.slider("Cantidad de meses")
        date_input = [first_date]
        next_date = first_date
        for i in range(months):
            next_date += timedelta(months=1)
            date_input.append(next_date)


    

    if type(date_input) == list:
        smart_dates_sorter(0,len(date_input)-1,date_input)
    dict = {
        "Conos": cono,
        "Instructores": inst,
        "Moto Mary-Policia": mary,
        "Vehiculo Interceptor": inter,
        "Vehiculo Z4": z4
    }
    new_event = Event(date_input,time_input,"Práctica de Conducción",dict,place)

    
    if col1.button("Cancelar",use_container_width=True):
        cambiar_pagina("inicio")
    if col3.button("Confirmar",use_container_width=True, type="primary", disabled= date_validation):
        agregar_evento(new_event)
        cambiar_pagina("inicio")

    
        
    
   
        

    
    
    

    
    # opciones_salida(new_event)
    