import streamlit as st
from recursos_eventos import *
from auxfunctions import *
from auxfunctions_2 import *
from datetime import datetime, date, time, timedelta


def practica_conduccion(editor=False,index=None):
    col0, col1 = st.columns([0.85,0.15], vertical_alignment="center")
    col2, col3 = st.columns([0.85,0.15], vertical_alignment="center")
    col4, col11, col5  = st.columns([0.51,0.34,0.15], vertical_alignment="center")
    col6, col7, col8 = st.columns([0.25,0.25,0.5],border=True)
    date_invalidation = True
    
    st.set_page_config(layout="wide")
    col0.header("PLANIFICACIÓN DE EVENTO",divider="red")
    col2.subheader("Entrenamientos: Práctica de Conducción", divider="red")
    
    with col4:
        repeticion = st.radio("Tipo de Horario y Repetición",
                    ["Evento único", "Repetición semanal", "Repetición mensual", "Rango de días"],
                    index=0, width="stretch", horizontal=True)
    
    
    with col7:        
        z4 = st.number_input("Cantidad de vehículos Z4",value=0, min_value=0, max_value=30)
        inter = st.number_input("Cantidad de vehículos Interceptor", value=0, min_value=0,max_value=5)
        mary = st.number_input("Cantidad de motos Mary-Policía", value=0, min_value=0, max_value=20)
    with col6:
        cono = st.number_input("Cantidad de conos", value=0, min_value=0, max_value=20)
        inst = st.number_input("Cantidad de Instructores", value=inter, min_value=inter, max_value= 30, help="Debe haber al menos un instructor por vehiculo" \
        " interceptor")
        option = ["Pista de automovilismo", "Centro de entrenamiento", "Academia Policial"]
        if inter > 0:
            option = [option[0]]
        place = st.selectbox("Lugar de práctica", option,
                     help="Por cuestiones de seguridad los vehículos Interceptor solo tienen permitido manejarse \n" \
                     "en la pista de automovilismo")
    
    
    if repeticion == "Evento único":
        date_input = col8.date_input("Fecha", value="today", min_value="today")
        time_1 = col8.time_input("Hora de inicio")
        time_2 = col8.time_input("Hora de conclusión")
        date_input = [date_input]

    elif repeticion == "Rango de días":
        date_input = col8.date_input("Rango de fechas", value=["today","today"], min_value="today")
        time_1 = col8.time_input("Hora de inicio")
        time_2 = col8.time_input("Hora de conclusión")
        

    elif repeticion == "Repetición semanal":
        col9, col10 = col8.columns([0.3,0.7])
        prechecks = [0,0,0,0,0,0,0]
        validations = [0,0,0,0,0,0,0]
        first_date = col10.date_input("Fecha inicial", value="today", min_value="today")
        time_1 = col10.time_input("Hora de inicio",value="now")
        time_2 = col10.time_input("Hora de conclusión",value="now")

        weekday = first_date.weekday()
        for i in range(7):
            if i == weekday:
                prechecks[i] = True
                validations[i] = True
        
        with col9:
            Mo = st.checkbox("Lunes", prechecks[0], disabled=validations[0])
            Tu = st.checkbox("Martes", prechecks[1], disabled=validations[1])
            We = st.checkbox("Miércoles", prechecks[2], disabled=validations[2])
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
        time_1 = col8.time_input("Hora de inicio")
        time_2 = col8.time_input("Hora de conclusión")        
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
        "Moto Mary-Policía": mary,
        "Vehículo Interceptor": inter,
        "Vehículo Z4": z4
    }
    new_event = Event(date_input,(time_1,time_2),"Práctica de Conducción",dict,place)
    
    resources = st_resources()
    collitions_list = collition_search(new_event,resources)
    st.write(st_resources())
    if not collitions_list:
       date_invalidation = False

    with col11.popover("Colisiones e Intervalos", width="stretch"):
        
        st.warning("Colisiones")
        st.markdown(f"""<div style='
                border: 2px solid red;
                color: darkred;
                border-radius: 8px;
                text-align: center;
                '>{decoding_collitions(collitions_list,new_event)}
                </div>""",unsafe_allow_html=True)
        st.success("Próximo intervalo disponible:")
        st.markdown(f"""<div style='
                    border: 1.5px solid darkgreen;
                    border-radius: 8px;
                    color: darkgreen;
                    text-align: center;
                    '>{next_gap()}
                    </div>""",unsafe_allow_html=True)

    
    if col1.button("Cancelar",use_container_width=True):
        cambiar_pagina("inicio")
    if col3.button("Confirmar",use_container_width=True, type="primary", disabled= date_invalidation):
        agregar_evento(new_event)
        agregar_fecha(date_input)
        dict_dates = st.session_state.dates
        for i in range(len(dict_dates)):
            dict_dates[i] = date_event_dict(dict_dates[i])
        dict_events = st.session_state.events
        for i in range(len(dict_events)):
            dict_events[i] = dict_events[i].to_dict()
        
        storage = [dict_dates,dict_events]
        save_json(storage,"data.json")
        cambiar_pagina("inicio")
    
    
        
    
   
        

    
    
    

    
    # opciones_salida(new_event)
    