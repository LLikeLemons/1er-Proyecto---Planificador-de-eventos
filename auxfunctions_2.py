import os
import sys
import json
from recursos_eventos import Event
from datetime import date, time

#========================================================================================================================
def obtain_path(archivo):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, archivo)

def load_json(nombre_archivo):
    path = obtain_path(nombre_archivo)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR>No se encuentra el archivo {nombre_archivo}")
        return [[],[]]
    
def save_json(datos,nombre_archivo):
    if getattr(sys, 'frozen', False):
        path = os.path.join(os.path.dirname(sys.executable),nombre_archivo)
    else:
        path = os.path.join(os.path.dirname(__file__), nombre_archivo)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(datos,f,indent=4, ensure_ascii=False)
        return path


#=============================================================================================================================
