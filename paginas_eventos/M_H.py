import streamlit as st
from methods import *
from datetime import datetime, date, time, timedelta

def manejo_helicoptero(editor=False,editable_event=None, index=None):
    col0, col1 = st.columns([0.85,0.15], vertical_alignment="center")
    col2, col3 = st.columns([0.85,0.15], vertical_alignment="center")
    col4, col11, col5  = st.columns([0.51,0.34,0.15], vertical_alignment="center")
    col6, = st.columns(1)    
    col7, col8 = st.columns([0.5,0.5],border=True)
    tab1, tab2 = col7.tabs(["Recursos predeterminados","Recursos personalizados"])
    tab3, = col8.tabs(["Fecha y Hora"])
    date_invalidation = False
    actual_datetime = datetime.now()
    actual_date = date(actual_datetime.year,actual_datetime.month,actual_datetime.day)
    actual_time = time(actual_datetime.hour,actual_datetime.minute)  
    clock = False
    
    col0.header("PLANIFICACIÓN DE EVENTO",divider="red")
    col2.subheader("Cursos de Capacitación: Manejo de Helicóptero", divider="red")

#=========| VARIABLES DE EDITOR PARA CONFIGURACION PREDETERMINADA   |=============================================================================
    frecuency_options = ["Evento único", "Frecuencia semanal", "Frecuencia mensual", "Rango de días"]
    places_options = ["Centro de entrenamiento", "Aula 1", "Aula 2", "Aula 3"]
    if editor:
        
        index_variable = frecuency_options.index(editable_event.frecuency_type)
        heli_variable = editable_event.resources["Helicóptero"]
        inst_variable = editable_event.resources["Instructores"]
        man_variable = editable_event.resources["Manuales de conducción para agentes"]
        proy_variable = editable_event.resources["Proyectores"]
        place_variable = editable_event.place
        time_variable1 = editable_event.time[0]
        time_variable2 = editable_event.time[1]
        frecuency_variable = editable_event.frecuency
        first_date_variable = editable_event.date[0]
        tuple_date_variable = (editable_event.date[0],editable_event.date[-1])
        if heli_variable > 0:
            default = "Capacitación Práctica"
        else:
            default = "Capacitación Teórica"
            heli_variable = 1
        defaultcr = [] 
        custom_keys = st.session_state.custom_resources.keys()
        for k in editable_event.resources.keys():
            if k in custom_keys:
                defaultcr.append(k) 
    else:
        index_variable = 0
        heli_variable = 1
        inst_variable = 0
        man_variable = 0
        proy_variable = 0
        place_variable = "Aula 1"
        time_variable1 = "now"
        time_variable2 = "now"
        frecuency_variable = 0
        first_date_variable = "today"
        tuple_date_variable = ["today","today"]
        default = "Capacitación Teórica"
        defaultcr = None


    #============|  TIPO DE FRECUENCIAS   |========================================================================================================
    with col4:
        frecuency_type = st.radio("Tipo de Horario y Repetición",
                    frecuency_options,
                    index=index_variable, width="stretch", horizontal=True)
    
    #============|   CONFIGURACION DE RECURSOS   |==================================================================================================
    training = col6.select_slider("Tipo de Capacitación:",options=["Capacitación Teórica","Capacitación Práctica"],
                                width="stretch",label_visibility= "collapsed", value=default)
    with tab1:  
        if training == "Capacitación Teórica":   
            heli = 0      
            inst = st.number_input("Cantidad de instructores", value=inst_variable, min_value=0,max_value=30)
            man = st.number_input("Cantidad de manuales de conducción para agentes", value=man_variable, min_value=0, max_value=50)
            proy = st.number_input("Cantidad de proyectores", value=proy_variable, min_value=0, max_value=5)            
            places_options1 = places_options[1:]  
            if place_variable != "Centro de entrenamiento":
                place_index = places_options1.index(place_variable)
            else:
                place_index = 0
        else:
            man = 0
            proy = 0
            heli = st.number_input("Cantidad de helicópteros", value=heli_variable, min_value=1,max_value=2)
            inst = st.number_input("Cantidad de instructores", value=heli, min_value=heli,max_value=30)            
            places_options1 = places_options[0] 
            place_index = 0 
    with tab2: 
        custom_resources = st.multiselect("I THINK IT IS OK", list(st.session_state.custom_resources.keys()),label_visibility="collapsed",default=defaultcr)
        custom_dict = {}
        for i in range(len(custom_resources)):
            custom_dict[custom_resources[i]] = st.number_input(f"Cantidad de {custom_resources[i]}",step=1,min_value=0,
                                                               max_value=st.session_state.custom_resources[custom_resources[i]],
                                                               value=editable_event.resources[custom_resources[i]] if defaultcr else 0)

        
    place = st.selectbox("Lugar de práctica", places_options1,index=place_index)
        

    #======|   AYUDA A RESTRICCIONES   |===========================================================================================================
    
    
    date_help = "Las fechas no pueden ser domingos"
    time1_help = "Las hora de inicio y conclusion no pueden ser menores o iguales que la hora actual si está marcada la fecha actual"
    time2_help = "La hora de conclusion no puede ser menor o igual que la hora de inicio"
    

    #=====|   CONFIGURACION POR TIPO DE FRECUENCIA   |=============================================================================================
    frecuency = 0
    validations = [0,0,0,0,0,0,0]
    attempts = [0,0,0,0,0,0,0]
    if frecuency_type == "Evento único":
        first_date = tab3.date_input("Fecha", value=first_date_variable , min_value="today", help = date_help)
        time_1 = tab3.time_input("Hora de inicio", value= time_variable1, help=time1_help)
        time_2 = tab3.time_input("Hora de conclusión", value= time_variable2, help=time2_help)
        date_input = [first_date]

    elif frecuency_type == "Rango de días":
        range_input = tab3.date_input("Rango de fechas", value=tuple_date_variable, min_value="today", help= "Se descartarán todas las fechas del intervalo que sean domingo")
        first_date = range_input[0]
        time_1 = tab3.time_input("Hora de inicio", value= time_variable1, help=time1_help)
        time_2 = tab3.time_input("Hora de conclusión", value= time_variable2, help=time2_help)
        if len(range_input) == 2 and range_input[0] != range_input[-1]:
            date_input = range_addition(range_input)
        else:
            date_input = [first_date]
            frecuency_type = "Evento único"
        

    elif frecuency_type == "Frecuencia semanal":
        col9, col10 = tab3.columns([0.3,0.7])
        prechecks = [0,0,0,0,0,0,0]
        
        first_date = col10.date_input("Fecha inicial", value=first_date_variable, min_value="today", help=date_help)

        time_1 = col10.time_input("Hora de inicio",value= time_variable1,  help=time1_help)
        time_2 = col10.time_input("Hora de conclusión",value= time_variable2,  help=time2_help)

        weekday = first_date.weekday()
        if editor:
            prechecks = editable_event.week_days
            validations[editable_event.date[0].weekday()] = True
        else:            
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
            Sa = st.checkbox("Sábado", prechecks[5], disabled=validations[5])
        frecuency = col5.slider("Cantidad de semanas",value=frecuency_variable, max_value=12)
        attempts = [Mo,Tu,We,Th,Fr,Sa]
        date_input = []
        next_date = first_date
        for i in range(len(attempts)):
            if attempts[i]:
                next_date = first_date + timedelta(days=(i-weekday)%7)
                date_input.append(next_date)
                for j in range(frecuency):
                    next_date += timedelta(days=7)
                    date_input.append(next_date)
        

    elif frecuency_type == "Frecuencia mensual":            
        first_date = tab3.date_input("Fecha inicial", value=first_date_variable, min_value="today", help=date_help)
        
        time_1 = tab3.time_input("Hora de inicio",value= time_variable1, help=time1_help)
        time_2 = tab3.time_input("Hora de conclusión",value= time_variable2, help=time2_help)        
        frecuency = col5.slider("Cantidad de meses",value=frecuency_variable,max_value=12)
        date_input = [first_date]
        next_date = first_date
        for i in range(frecuency):
            next_date = date(next_date.year,next_date.month+1,next_date.day)
            date_input.append(next_date)


#========|   CREACION DEL EVENTO   |===============================================================================================================

    if type(date_input) == list:
        smart_dates_sorter(0,len(date_input)-1,date_input)
    dict = {
        "Helicóptero": heli,
        "Instructores": inst,
        "Manuales de conducción para agentes": man,
        "Proyectores": proy
    }
    dict.update(custom_dict)
    new_event = Event(date_input,(time_1,time_2),"Manejo de Helicóptero",dict,place,frecuency_type,frecuency,attempts)
    
#==========|   BUSQUEDA DE COLISIONES E INVALIDACION DEL EVENTO   |===============================================================================
    resources = st.session_state.resources
    collitions_list = collition_search(new_event,resources,editor=editor,index=index,editable_event=editable_event)
    if collitions_list:
       date_invalidation = True

    
    if time_2 <= time_1 or ((time_1 <= actual_time or time_2 <= actual_time) and first_date == actual_date):
        date_invalidation = True
        clock = True

    if first_date.weekday() == 6:
        date_invalidation = True
        clock = True
#==========|   MUESTRA DE COLISIONES   |============================================================================================================
    with col11.popover("Colisiones e Intervalos", width="stretch", help="La sugerencia del próximo intervalo disponible se hace teniendo"
    " en cuenta los recursos, cada detalle del tipo de frecuencia y el horario incluidos, exceptuando la fecha inicial escogida"):
        if collitions_list:
            st.warning("Colisiones")
            st.markdown(f"""<div style='
                    border: 2px solid #8e5e24;
                    color: #8e5e24;
                    border-radius: 8px;
                    text-align: center;
                    '>{decoding_collitions(collitions_list,new_event)}
                    </div>""",unsafe_allow_html=True)
        st.success("Próximo intervalo disponible:")
        st.markdown(f"""<div style='
                    border: 1.5px solid #1b865d;
                    border-radius: 8px;
                    color: #1b865d;
                    text-align: center;
                    '>{next_gap(new_event,resources,editor,index) if not clock else "Valide primero el horario o  <br> deseleccione domingo como fecha"}
                    </div>""",unsafe_allow_html=True)

#============|   BOTONES DE ACCION   |==============================================================================================================
    if col1.button("Cancelar",use_container_width=True):
        cambiar_pagina("inicio")
        st.rerun()
    if col3.button("Confirmar",use_container_width=True, type="primary", disabled= date_invalidation):
        if editor:
            del st.session_state.events[index]
            st.session_state.dates = recalibrate_dates_index(index,st.session_state.dates)
        agregar_evento(new_event)
        agregar_fecha(date_input)
        dict_dates = deepcopy(st.session_state.dates)
        for i in range(len(dict_dates)):
            dict_dates[i] = date_event_dict(dict_dates[i])
        dict_events = deepcopy(st.session_state.events)
        for i in range(len(dict_events)):
            dict_events[i] = dict_events[i].to_dict()
        
        storage = [dict_dates,dict_events,st.session_state.resources,st.session_state.custom_resources]
        save_json(storage,"data.json") 
        cambiar_pagina("inicio")    
        st.rerun()