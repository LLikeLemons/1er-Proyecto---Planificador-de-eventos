import os
import sys
import json
from .recursos_eventos import Event
from datetime import date, time

#========|  CARGA Y GUARDA DE DATOS   |============================================================================================================
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


#=====|   ALMACEN DE RECURSOS   |========================================================================================================================
def st_resources():
        return {
    "AMP": 50,
    "Bicicletas": 30,
    "Blancos de práctica": 30,
    "Chalecos Antibalas":100,
    "Conos": 20,
    "Entrenadores de Defensa Personal":5,
    "Entrenadores Físicos":5,
    "Equipo Táctico":20,
    "Escopetas": 50,
    "Instructores": 30,
    "Instructores de unidades especiales":6,
    "Libro de capacitación para agentes I":50,
    "Libro de capacitación para agentes II":50,
    "Manuales de conducción para agentes": 50,
    "Moto Mary-Policía": 20,
    "Oficiales de alto rango": 7,
    "Proyectores": 10,
    "Vehículo Z4": 30,
    "Vehículo Interceptor": 5,
    }

