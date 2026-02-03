import streamlit as st
from methods import *
from datetime import datetime, date, time, timedelta

def intervencion_domicilio(editor=False,editable_event=None, index=None):
    col0, col1 = st.columns([0.85,0.15], vertical_alignment="center")
    col2, col3 = st.columns([0.85,0.15], vertical_alignment="center")
    col4, col11, col5  = st.columns([0.51,0.34,0.15], vertical_alignment="center")
    col6, col8 = st.columns([0.5,0.5],border=True)
    tab1, tab2, tab3 = col6.tabs(["Armamento","Equipaje","Oficiales"])
    tab4, = col8.tabs(["Fecha y hora"])
    date_invalidation = False
    actual_datetime = datetime.now()
    actual_date = date(actual_datetime.year,actual_datetime.month,actual_datetime.day)
    actual_time = time(actual_datetime.hour,actual_datetime.minute)  
    clock = False
    
    col0.header("PLANIFICACIÓN DE EVENTO",divider="red")
    col2.subheader("Simulacros: Intervención a Domicilio", divider="red")

#=========| VARIABLES DE EDITOR PARA CONFIGURACION PREDETERMINADA   |=============================================================================
    frecuency_options = ["Evento único", "Frecuencia semanal", "Frecuencia mensual"]
    places_options = ["Domicilio preparado"]
    if editor:
        
        index_variable = frecuency_options.index(editable_event.frecuency_type)
        ar_variable = editable_event.resources["Oficiales de alto rango"]
        inst_variable = editable_event.resources["Instructores"]
        z4_variable = editable_event.resources["Vehículo Z4"]
        equip_variable = editable_event.resources["Equipaje Táctico"]
        chal_variable = editable_event.resources["Chalecos Antibalas"]
        pist_variable = editable_event.resources["Pistolas"]
        amp_variable = editable_event.resources["AMP"]
        esc_variable = editable_event.resources["Escopetas"]

        place_variable = places_options.index(editable_event.place)
        time_variable1 = editable_event.time[0]
        time_variable2 = editable_event.time[1]
        frecuency_variable = editable_event.frecuency
        first_date_variable = editable_event.date[0]
    else:
        index_variable = 0
        ar_variable = 1
        inst_variable = 0
        equip_variable = 0
        chal_variable = 0
        pist_variable = 0
        amp_variable = 0
        esc_variable = 0
        z4_variable = 0
        place_variable = 0
        time_variable1 = "now"
        time_variable2 = "now"
        frecuency_variable = 0
        first_date_variable = "today"
        tuple_date_variable = ["today","today"]


    #============|  TIPO DE FRECUENCIAS   |========================================================================================================
    with col4:
        frecuency_type = st.radio("Tipo de Horario y Repetición",
                    frecuency_options,
                    index=index_variable, width="stretch", horizontal=True)
    
    #============|   CONFIGURACION DE RECURSOS   |==================================================================================================    
        
    
    with tab1:
        pist = st.number_input("Cantidad de pistolas", value=pist_variable, min_value=0, max_value=20)
        amp = st.number_input("Cantidad de AMP", value=amp_variable, min_value=0, max_value=20)
        esc = st.number_input("Cantidad de escopetas", value=esc_variable, min_value=0, max_value=20)
    with tab2:    
        z4 = st.number_input("Cantidad de vehículos Z4",value=z4_variable, min_value=0, max_value=30)
        equip = st.number_input("Cantidad de equipaje táctico", value=equip_variable, min_value=0, max_value=20)
        chal = st.number_input("Cantidad de chalecos", value=chal_variable, min_value=0, max_value=20)
    with tab3:
        inst = st.number_input("Cantidad de instructores", value=inst_variable, min_value=0, max_value= 30)        
        ar = st.number_input("Cantidad de oficiales de alto rango", value=ar_variable, min_value=0,max_value=5)
        place = st.selectbox("Lugar de simulacro", places_options,index=place_variable)
        

    #======|   AYUDA A RESTRICCIONES   |===========================================================================================================
    
    
    date_help = "Las fechas no pueden ser domingos"
    time1_help = "Las hora de inicio y conclusión no pueden ser menores o iguales que la hora actual si está marcada la fecha actual"
    time2_help = "La hora de conclusión no puede ser menor o igual que la hora de inicio"
    

    #=====|   CONFIGURACION POR TIPO DE FRECUENCIA   |=============================================================================================
    frecuency = 0
    validations = [0,0,0,0,0,0,0]
    attempts = [0,0,0,0,0,0,0]
    if frecuency_type == "Evento único":
        first_date = tab4.date_input("Fecha", value=first_date_variable , min_value="today", help = date_help)
        time_1 = tab4.time_input("Hora de inicio", value= time_variable1, help=time1_help)
        time_2 = tab4.time_input("Hora de conclusión", value= time_variable2, help=time2_help)
        date_input = [first_date]
        

    elif frecuency_type == "Frecuencia semanal":
        col9, col10 = tab4.columns([0.3,0.7])
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
        first_date = tab4.date_input("Fecha inicial", value=first_date_variable, min_value="today", help=date_help)
        
        time_1 = tab4.time_input("Hora de inicio",value= time_variable1, help=time1_help)
        time_2 = tab4.time_input("Hora de conclusión",value= time_variable2, help=time2_help)        
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
        "AMP": amp,
        "Chalecos Antibalas": chal,        
        "Equipaje Táctico": equip,
        "Escopetas": esc,
        "Instructores": inst,
        "Oficiales de alto rango": ar,
        "Pistolas": pist,
        "Vehículo Z4": z4
    }
    new_event = Event(date_input,(time_1,time_2),"Intervención a Domicilio",dict,place,frecuency_type,frecuency,attempts)
    
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
