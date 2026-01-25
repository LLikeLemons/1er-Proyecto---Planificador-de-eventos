import streamlit as st
from methods import *
from datetime import datetime, date, time, timedelta
#PENDIENTE AJUSTAR LOS RECURSOS
def entrenamiento_fisico(editor=False,editable_event=None, index=None):
    col0, col1 = st.columns([0.85,0.15], vertical_alignment="center")
    col2, col3 = st.columns([0.85,0.15], vertical_alignment="center")
    col4, col11, col5  = st.columns([0.51,0.34,0.15], vertical_alignment="center")
    col7, = st.columns(1)
    col6, col8 = st.columns([0.5,0.5],border=True)   
 
    date_invalidation = False
    actual_datetime = datetime.now()
    actual_date = date(actual_datetime.year,actual_datetime.month,actual_datetime.day)
    actual_time = time(actual_datetime.hour,actual_datetime.minute)  
    clock = False
    
    col0.header("PLANIFICACIÓN DE EVENTO",divider="red")
    col2.subheader("Entrenamientos: Entrenamiento Físico", divider="red")

#=========| VARIABLES DE EDITOR PARA CONFIGURACION PREDETERMINADA   |=============================================================================
    frecuency_options = ["Evento único", "Frecuencia semanal", "Frecuencia mensual", "Rango de días"]
    places_options = ["Salón de Artes Marciales","Centro de entrenamiento", "Academia Policial"]
    if editor:       
        index_variable = frecuency_options.index(editable_event.frecuency_type)
        ef_variable = editable_event.resources["Entrenadores Físicos"]
        ed_variable = editable_event.resources["Entrenadores de Defensa Personal"]
        bic_variable = editable_event.resources["Bicicletas"]
        place_variable = editable_event.place
        time_variable1 = editable_event.time[0]
        time_variable2 = editable_event.time[1]
        frecuency_variable = editable_event.frecuency
        first_date_variable = editable_event.date[0]
        tuple_date_variable = editable_event.date[0]
        if ef_variable > 0:
            default = "Físico"
        else:
            default = "Defensa Personal"
    else:
        index_variable = 0
        ef_variable = 0
        ed_variable = 0
        bic_variable = 0
        place_variable = 0
        time_variable1 = "now"
        time_variable2 = "now"
        frecuency_variable = 0
        first_date_variable = "today"
        tuple_date_variable = ["today","today"]
        default = "Físico"

    #============|  TIPO DE FRECUENCIAS   |========================================================================================================
    with col4:
        frecuency_type = st.radio("Tipo de Horario y Repetición",
                    frecuency_options,
                    index=index_variable, width="stretch", horizontal=True)
    
    #============|   CONFIGURACION DE RECURSOS   |==================================================================================================    
    training = col7.select_slider("Tipo de Entrenamiento",options=["Físico","Defensa Personal"],width="stretch",label_visibility= "collapsed",value=default)   
    with col6: 
        if training == "Físico":
            ef = st.number_input("Cantidad de entrenadores físicos",value=ef_variable, min_value=0, max_value=3)
            ed = 0
            places_options1 = places_options[1:]
            place_variable = places_options1.index(place_variable)
        else: 
            ed = st.number_input("Cantidad de entrenadores de Defensa Personal", value=ed_variable, min_value=0,max_value=2)
            ef = 0
            places_options1 = places_options[0]
            place_variable = 0
        bic = st.number_input("Cantidad de bicicletas", value=bic_variable, min_value=0, max_value=20)
            
        place = st.selectbox("Lugar de entrenamiento", places_options1,index=place_variable)
        

    #======|   AYUDA A RESTRICCIONES   |===========================================================================================================
    
    
    date_help = "Las fechas no pueden ser domingos"
    time1_help = "Las hora de inicio y conclusión no pueden ser menores o iguales que la hora actual si está marcada la fecha actual"
    time2_help = "La hora de conclusión no puede ser menor o igual que la hora de inicio"
    

    #=====|   CONFIGURACION POR TIPO DE FRECUENCIA   |=============================================================================================
    frecuency = 0
    validations = [0,0,0,0,0,0,0]
    attempts = [0,0,0,0,0,0,0]
    if frecuency_type == "Evento único":
        first_date = col8.date_input("Fecha", value=first_date_variable , min_value="today", help = date_help)
        time_1 = col8.time_input("Hora de inicio", value= time_variable1, help=time1_help)
        time_2 = col8.time_input("Hora de conclusión", value= time_variable2, help=time2_help)
        date_input = [first_date]

    elif frecuency_type == "Rango de días":
        range_input = col8.date_input("Rango de fechas", value=tuple_date_variable, min_value="today", help= "Se descartarán todas las fechas del intervalo que sean domingo")
        first_date = range_input[0]
        time_1 = col8.time_input("Hora de inicio", value= time_variable1, help=time1_help)
        time_2 = col8.time_input("Hora de conclusión", value= time_variable2, help=time2_help)
        if len(range_input) == 2:
            date_input = range_addition(range_input)
        else:
            date_input = [first_date]
            frecuency_type = "Evento único"
        

    elif frecuency_type == "Frecuencia semanal":
        col9, col10 = col8.columns([0.3,0.7])
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
        first_date = col8.date_input("Fecha inicial", value=first_date_variable, min_value="today", help=date_help)
        
        time_1 = col8.time_input("Hora de inicio",value= time_variable1, help=time1_help)
        time_2 = col8.time_input("Hora de conclusión",value= time_variable2, help=time2_help)        
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
        "Bicicletas": bic,
        "Entrenadores de Defensa Personal": ed,
        "Entrenadores Físicos": ef        
    }
    new_event = Event(date_input,(time_1,time_2),"Entrenamiento Físico",dict,place,frecuency_type,frecuency,attempts)
    
#==========|   BUSQUEDA DE COLISIONES E INVALIDACION DEL EVENTO   |===============================================================================
    resources = st_resources()
    collitions_list = collition_search(new_event,resources,editor=editor,index=index,editable_event=editable_event)
    if collitions_list:
       date_invalidation = True

    
    if time_2 <= time_1 or ((time_1 <= actual_time or time_2 <= actual_time) and first_date == actual_date):
        date_invalidation = True
        clock = True

    if first_date.weekday() == 6:
        date_invalidation = True
        clock = True   #====sdafsefasdfa
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
        
        storage = [dict_dates,dict_events]
        save_json(storage,"data.json") 
        cambiar_pagina("inicio")    