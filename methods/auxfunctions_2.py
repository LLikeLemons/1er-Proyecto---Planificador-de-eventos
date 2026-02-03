import os
import sys
import json
import streamlit as st
from .recursos_eventos import Event, date_event_dict
from datetime import date, time
from pathlib import Path
from copy import deepcopy

#========|  CARGA Y GUARDA DE DATOS   |============================================================================================================
STORAGE_DIR_NAME = "data"
def _project_root() -> Path:
    # si este archivo está dentro de methods/, parents[1] es la raíz del proyecto
    return Path(__file__).resolve().parents[1]

def _storage_dir() -> Path:
    p = _project_root() / STORAGE_DIR_NAME
    p.mkdir(parents=True, exist_ok=True)
    return p

def storage_path(filename: str) -> Path:
    # si pasan una ruta absoluta, la usamos tal cual; si no, la colocamos en la carpeta de datos
    f = Path(filename)
    if f.is_absolute():
        return f
    return _storage_dir() / filename

def save_json(data, filename: str = "data.json", encoding: str = "utf-8") -> str:
    path = storage_path(filename)
    with open(path, "w", encoding=encoding) as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    return str(path)

def load_json(filename: str = "data.json", encoding: str = "utf-8"):
    path = storage_path(filename)
    if not path.exists():
        # estructura por defecto esperada por la app; ajusta si tu app espera otra
        default = [[], [],{},{}]
        save_json(default, filename, encoding=encoding)
        return default
    with open(path, "r", encoding=encoding) as fh:
        return json.load(fh)

#=====|   ALMACEN DE RECURSOS   |========================================================================================================================

def st_resources_edit(resources,amount,delete=False):
    if not delete:
        st.session_state.resources[resources] = amount
        st.session_state.custom_resources[resources] = amount
    else:
        del st.session_state.resources[resources]
        del st.session_state.custom_resources[resources]
    dict_dates = deepcopy(st.session_state.dates)
    for i in range(len(dict_dates)):
        dict_dates[i] = date_event_dict(dict_dates[i])
    dict_events = deepcopy(st.session_state.events)
    for i in range(len(dict_events)):
        dict_events[i] = dict_events[i].to_dict()
    
    storage = [dict_dates,dict_events,st.session_state.resources,st.session_state.custom_resources]
    save_json(storage,"data.json") 
    
def deletion_validation(resource):
    for i in range(len(st.session_state.events)):
        if resource in st.session_state.events[i].resources.keys():
            return False
    return True


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////