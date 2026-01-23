import streamlit as st
from copy import deepcopy
def recalibrate_dates_index(index,dates_list):
    pre = deepcopy(dates_list)
    pre2 = []
    for i in range(len(pre)):
        if pre[i][1] > index:
            pre2.append((pre[i][0],pre[i][1]-1))
        elif pre[i][1] < index:
            pre2.append((pre[i][0],pre[i][1]))

    return pre2