import PySimpleGUI as sg

list_1 = [i for i in range(1,6)]
list_2 = [i for i in 'abcde']

layout_1=[[sg.LB(list_1)]]
layout_2=[[sg.LB(list_2)]]

layout = [
    [sg.TabGroup([[sg.Tab('AC_FUN',layout_1)]])]
    ]