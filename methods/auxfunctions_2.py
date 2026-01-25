import os
import sys
import json
from .recursos_eventos import Event
from datetime import date, time
from pathlib import Path

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
        default = [[], []]
        save_json(default, filename, encoding=encoding)
        return default
    with open(path, "r", encoding=encoding) as fh:
        return json.load(fh)

#=====|   ALMACEN DE RECURSOS   |========================================================================================================================
def st_resources():
        return {
    "AMP": 50,
    "Bicicletas": 20,
    "Blancos de práctica": 30,
    "Chalecos Antibalas":100,
    "Conos": 20,
    "Entrenadores de Defensa Personal":2,
    "Entrenadores Físicos":3,
    "Equipaje Táctico":20,
    "Escopetas": 50,
    "Helicóptero":2,
    "Instructores": 30,
    "Instructores de unidades especiales":6,
    "Libro de capacitación para agentes I":50,
    "Libro de capacitación para agentes II":50,
    "Manuales de conducción para agentes": 50,
    "Moto Mary-Policía": 20,
    "Oficiales de alto rango": 7,
    "Pistolas": 70,
    "Proyectores": 5,
    "Vehículo Z4": 30,
    "Vehículo Interceptor": 5,
    }

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////