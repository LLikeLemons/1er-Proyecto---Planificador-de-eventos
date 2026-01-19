import streamlit as st
from datetime import date, datetime, time
from recursos_eventos import Event

def binary_search(left: int, right: int, list: list[tuple[date,int]], element: date):
    indexes = [0,0]
    main_indexes = []
    if list[0][0] == element:
        indexes[0] = 0
    else:
        indexes[0] = binary_search_first(left, right, list, element)
    if list[len(list)-1][0] == element:
        indexes[1] = len(list)-1
    else:
        indexes[1] = binary_search_last(left, right, list, element)
    if indexes[0] == -1:
        return False
    for i in range(indexes[0],indexes[1]):
        main_indexes.append(list[i][1])
    return main_indexes

def binary_search_first(left: int, right: int, list: list[tuple[date,int]], element: date):
    if left > right or (left == right and (right == len(list)-1 or list[right+1][0] != element)):
        return -1
    middle = (left+right)//2
    if list[middle][0] != element and list[middle+1][0] == element:
        return middle+1
    elif list[middle][0] >= element:
        return binary_search_first(left, middle, list, element)
    else:
        return binary_search_first(middle+1,right,list,element)
    
def binary_search_last(left: int, right: int, list: list[tuple[date,int]], element: date):
    if left > right or (left == right and list[right-1][0] != element):
        return -1
    middle = (left+right)//2
    if list[middle][0] != element and list[middle-1][0] == element:
        return middle-1
    elif list[middle][0] <= element:
        return binary_search_last(middle+1, right, list, element)
    else:
        return binary_search_last(left,middle,list,element)

#-------------------------------------------------------------------------------------------------------------------------------

# def hours_collition(second_event_time: time, main_event_time: time):
#     se = second_event_time, me = main_event_time
#     if me[0] >= se[1] or me[1] <= se[0]:
#         return False
#     return True

# def manage_resources(total_resources: dict[int], event_resources:dict[int]):
#     for k in event_resources.keys():
#         total_resources[k] -= event_resources[k]

# def resource_collition(total_resources: dict[int], event_resources: dict[int]):
#     collition = False
#     for k in event_resources.keys():
#         total_resources[k] -= event_resources[k]
#         if total_resources[k] < 0:
#             collition = True
#     return collition
# def collition_search(event,ssdates,ssresources,ssevents):
#     collitions_result = []
#     if st.session_state.dates:
#         for i in range(len(event.date)):
#             total_resources = st.session_state.resources
#             avaliable_place = True
#             values_list = binary_search(0,len(st.session_state.dates)-1,st.session_state.dates, event.date[i])        
#             if values_list:   
#                 for j in range(len(values_list)):
#                     if hours_collition(st.session_state.events[values_list[j]].time, event.time):
#                         manage_resources(total_resources,st.session_state.events[values_list[j]].resources)
#                         if st.session_state.events[values_list[j]].place == event.place:
#                             avaliable_place = False
#                 if resource_collition(total_resources,event.resources):
#                     collitions_result.append((event.date[i],total_resources,avaliable_place))
#                 elif not avaliable_place:
#                     collitions_result.append(event.date[i],-1, False)            
#         return collitions_result
#     else:
#         return collitions_result
# dict = {
#     "Conos": 0,
#     "Instructores": 3,
#     "Moto Mary-Policía": 0,
#     "Vehículo Interceptor": 0,
#     "Vehículo Z4": 0
# }
# new_event = Event(date(2026,1,19),(time(0,10),time(0,50)), "Practica de Conduccion",dict)

# resources = {
#     "AMP": 50,
#     "Bicicletas": 30,
#     "Blancos de práctica": 30,
#     "Chalecos Antibalas":100,
#     "Conos": 20,
#     "Entrenadores de Defensa Personal":5,
#     "Entrenadores Físicos":5,
#     "Equipo Táctico":20,
#     "Escopetas": 50,
#     "Instructores": 30,
#     "Instructores de unidades especiales":6,
#     "Libro de capacitación para agentes I":50,
#     "Libro de capacitación para agentes II":50,
#     "Manuales de conducción para agentes": 50,
#     "Moto Mary-Policía": 20,
#     "Oficiales de alto rango": 7,
#     "Proyectores": 10,
#     "Vehículo Z4": 30,
#     "Vehículo Interceptor": 5,
# }
# ssdates = [(date(2026, 1, 19), 1)]
# ssevents = [Event(date(2026,1,19),(time(0,29),time(0,40)), "Practica de Conduccion",dict)
# ]

# print(collition_search(new_event),ssdates,resources,ssevents)
print(list(range(0,0+1)))