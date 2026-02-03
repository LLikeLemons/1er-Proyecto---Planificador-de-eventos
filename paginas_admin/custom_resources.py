import streamlit as st
from methods import *

def custom_resources():
    st.markdown("""<div style='
                font-size: 80px;
                text-align: center;
                '>RECURSO PERSONALIZADO
                </div>""",unsafe_allow_html=True)
    st.markdown("""<div style='border-top: 4px solid ;
                border-image: linear-gradient(45deg, blue, lightblue) 1;
                '></div>""",unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)
    new_resource = col4.text_input("Nombre del Recurso")
    new_amount = col5.number_input("Cantidad del evento a agregar",0)
    edit_amount = col6.number_input("Cantidad del evento a editar",0)
    options = []

    col1, col2, col3 = st.columns(3)
    for k,v in st.session_state.custom_resources.items():
        options.append(f"{k}: {v}")
    element = st.radio("Lista de elementos personalizados",options,horizontal=True)
    if element != None:
        index = options.index(element)
        c_resource = list(st.session_state.custom_resources.keys())[index]

    disabled = False
    not_addition = True
    if new_amount != 0 and new_resource != "":
        not_addition = False
    if not options or not deletion_validation(c_resource):
        disabled = True

    
    col1.button("Agregar",on_click=lambda: st_resources_edit(new_resource,new_amount),disabled=not_addition,type="primary",width="stretch")
    col2.button("Editar",on_click=lambda: st_resources_edit(c_resource,edit_amount),disabled= disabled, help="No puedes editar un recurso que esta incluido en al menos un evento",type="primary",width="stretch")
    col3.button("Eliminar",on_click=lambda: st_resources_edit(c_resource,delete=True),disabled= disabled,help="No puedes eliminar un recurso que esta incluido en al menos un evento",type="primary",width="stretch")
    
    