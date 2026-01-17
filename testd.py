import streamlit as st
from datetime import date, datetime, time

# col1, col2 = st.columns(2,border=True)
# tab1, tab2 = col1.tabs(["Hola","adios"])
# with tab1:
#     st.text_area("go")
# with tab2:
#     st.text_area("went")

# with col2:
#     st.text_area("hola")    

def binary_search_A(left: int, right: int, dates_list: list[tuple[date,int]], date: date):
    if left >= right and dates_list[right][0] != date:
        return []
    elif left >= right and dates_list[right][0] == date:
        return [right]
    middle = (left+right)//2
    if dates_list[middle][0] == date:
        irange = [0,0]
        irange[0] = aux_binary_search(left, middle, dates_list, date, under=True)
        irange[1] = aux_binary_search(middle+1, right, dates_list, date, under=False)
        new_range = []
        for i in range(irange[0],irange[1]+1):
            if dates_list[i][1] not in new_range:
                new_range.append(dates_list[i][1])
        return new_range
    elif dates_list[middle][0] > date:
        return binary_search(left, middle, dates_list, date)
    else:
        return binary_search(middle+1, right, dates_list, date)
        

def aux_binary_search(left: int, right: int, dates_list: list[tuple[date,int]], date: date, under: bool):
    middle = (left + right)//2
    if under:
        if dates_list[middle][0] == date and middle == 0:  
            return 0
        elif dates_list[middle][0] == date and middle != 0:        
            return  aux_binary_search(left, middle, dates_list, date, under)        
        elif dates_list[middle][0] < date and dates_list[middle+1][0] == date:
            return middle+1
        elif dates_list[middle][0] < date:
            return aux_binary_search(middle+1, right, dates_list, date, under)
    else:
        if dates_list[middle][0] == date and middle != len(dates_list)-1:        
            return aux_binary_search(middle+1, right, dates_list, date, under)
        elif dates_list[middle][0] == date and middle == len(dates_list)-1:
            return middle
        elif dates_list[middle][0] > date and dates_list[middle-1][0] == date:
            return middle-1
        elif dates_list[middle][0] > date:
            return aux_binary_search(left, middle, dates_list, date, under)
    

lista = [(date(2027,1,1),1),(date(2027,1,1),9),(date(2027,1,1),3),(date(2027,1,1),1),(date(2027,1,1),4)
         ,(date(2027,1,1),1),(date(2027,1,1),3),(date(2027,1,1),3),(date(2027,1,1),3),(date(2027,1,1),5),
         (date(2027,1,1),2),(date(2027,1,1),2),(date(2027,1,1),1),(date(2027,1,1),1)]
date1 = date(2028,1,1)

# indices = binary_search(0,len(lista)-1,lista, date1)
# print(indices)


def binary_search(left, right, list, element):
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
    for i in range(indexes[0],indexes[1]):
        main_indexes.append(list[i][1])
    return main_indexes

def binary_search_first(left,right,list,element):
    if left > right or (left == right and (right == len(list)-1 or list[right+1][0] != element)):
        return -1
    middle = (left+right)//2
    if list[middle][0] != element and list[middle+1][0] == element:
        return middle+1
    elif list[middle][0] >= element:
        return binary_search_first(left, middle, list, element)
    else:
        return binary_search_first(middle+1,right,list,element)
    
def binary_search_last(left,right,list,element):
    if left > right or (left == right and list[right-1][0] != element):
        return -1
    middle = (left+right)//2
    if list[middle][0] != element and list[middle-1][0] == element:
        return middle-1
    elif list[middle][0] <= element:
        return binary_search_last(middle+1, right, list, element)
    else:
        return binary_search_last(left,middle,list,element)


indices = binary_search(0,len(lista)-1,lista, date1)
print(indices)