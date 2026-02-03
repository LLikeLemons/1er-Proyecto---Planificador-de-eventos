import streamlit as st
from methods import *
from datetime import datetime, date, time, timedelta
from .opciones_admin import collition_search2
def resources_search():
    col9, = st.columns(1)
    col9.markdown("""<div style='
                border-bottom: 4px solid ;
                border-image: linear-gradient(45deg, blue, lightblue) 1;
                font-size: 80px;
                text-align: center;
                text-weight: bold;
                '>FECHAS Y RECURSOS
                </div>""",unsafe_allow_html=True)
    col4,col5,col6 = st.columns(3)
    date_input = col4.date_input("Fecha")
    time1 = col5.time_input("Hora de inicio")
    time2 = col6.time_input("Hora de conclusion")
    if time2 > time1:
        time_input = (time1,time2)
        resources = st.session_state.resources
        
        total_resources, total_places = collition_search2(date_input,time_input,resources)
        st.markdown("""<div style='
            border: 3px solid blue;
            border-radius: 7px;
            font-size: 15px;
            text-align: center;
            text-weight: bold;
            color: darkblue;
            '>Recursos disponibles
            </div>""",unsafe_allow_html=True)
        col1,col2,col3 = st.columns(3,border=True)
        i=0
        for k,v in total_resources.items():
            if i < 6:
                col1.markdown(f"""<div style='
                    border-bottom: 1px dashed darkblue;
                    text-size: 10px;
                    text-align: center;
                    '>{k}: {v}
                    </div>""",unsafe_allow_html=True)
            elif i < 13:
                col2.markdown(f"""<div style='
                    border-bottom: 1px dashed darkblue;
                    text-size: 10px;
                    text-align: center;
                    '>{k}: {v}
                    </div>""",unsafe_allow_html=True)
            else:
                col3.markdown(f"""<div style='
                    border-bottom: 1px dashed darkblue;
                    text-size: 10px;
                    text-align: center;
                    '>{k}: {v}
                    </div>""",unsafe_allow_html=True)
            i += 1
        st.markdown("""<div style='
            border: 3px solid blue;
            border-radius: 7px;
            font-size: 15px;
            text-align: center;
            text-weight: bold;
            color: darkblue;
            text-font: bold;
            '>Lugares disponibles
            </div>""",unsafe_allow_html=True)
        for v in total_places:
            st.markdown(f"""<div style='
                border-bottom: 1px dashed darkblue;
                text-size: 10px;
                text-align: center;
                '>{v}
                </div>""",unsafe_allow_html=True)
    else: 
        st.header("La hora de conclusion debe ser mayor que la hora de inicio")