import streamlit as st

def visualizador_eventos():
    st.markdown("""<div style='
                border-bottom: 4px solid ;
                border-image: linear-gradient(45deg, blue, lightblue) 1;
                font-size: 80px;
                text-align: center;
                text-weight: bold;
                '>VISUALIZADOR DE EVENTOS
                </div>""",unsafe_allow_html=True)
    col1, col2 = st.columns([0.85,0.15])
    if st.session_state.events:
        if len(st.session_state.events) == 1:
            index = 0
        else:     
            index = col2.number_input("Número del evento",min_value=1,max_value=len(st.session_state.events))-1
        event = st.session_state.events[index]
        col1.markdown(f"""<div style='
                    border-bottom: 4px double ;
                    border-image: linear-gradient(45deg, blue, lightblue) 1;
                    font-size: 40px;
                    text-weight: bold;
                    padding-left: 10px;
                    '>{event.type}
                    </div>""",unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.expander("Recursos",width="stretch"):
                for k,v in event.resources.items():
                    st.markdown(f"""<div style='
                        border-bottom: 1px dashed;
                        border-image: linear-gradient(45deg, blue, lightblue) 1;
                        text-align: center;
                        '>{k}: {v}
                        </div>""",unsafe_allow_html=True)
            
        with col2: 
            with st.expander(f"{event.frecuency_type}",width="stretch"):
                st.markdown(f"""<div style='
                        border-bottom: 1px dashed;
                        border-image: linear-gradient(45deg, blue, lightblue) 1;
                        font-size: 20px;
                        text-align: center;
                        '>Horario: {event.time[0]} - {event.time[1]}
                        </div>""",unsafe_allow_html=True)
                if event.frecuency_type == "Frecuencia mensual" or event.frecuency_type == "Frecuencia semanal":
                    st.markdown(f"""<div style='
                            border-bottom: 1px dashed;
                            border-image: linear-gradient(45deg, blue, lightblue) 1;
                            font-size: 20px;
                            text-align: center;
                            text-weight: bold;
                            '>Cantidad de repeticiones: {event.frecuency}
                            </div>""",unsafe_allow_html=True)
                if event.frecuency_type == "Frecuencia semanal":
                    string = ""
                    Weekdays = ["L ","Ma ","Mi ","J ","V ","S "]
                    for i in range(len(Weekdays)):
                        if event.week_days[i]:
                            string += Weekdays[i]
                    st.markdown(f"""<div style='
                            border-bottom: 1px dashed;
                            border-image: linear-gradient(45deg, blue, lightblue) 1;    
                            font-size: 20px;
                            text-align: center;
                            text-weight: bold;
                            '>Dias de la semana: {string.strip(" ")}
                            </div>""",unsafe_allow_html=True)
                st.markdown(f"""<div style='
                        border-bottom: 1px dashed;
                        border-image: linear-gradient(45deg, blue, lightblue) 1;
                        font-size: 20px;
                        text-align: center;
                        text-weight: bold;
                        '>Lugar: {event.place}
                        </div>""",unsafe_allow_html=True)
        with col3: 
            with st.expander("Fechas",width="stretch"):
                for i in range(len(event.date)):
                    st.markdown(f"""<div style='
                        border-bottom: 1px dashed;
                        border-image: linear-gradient(45deg, blue, lightblue) 1;
                        text-align: center;
                        '>{event.date[i]}
                        </div>""",unsafe_allow_html=True)
    else:
        st.write("Sin opciones disponibles")
