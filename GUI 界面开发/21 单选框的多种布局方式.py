import PySimpleGUI as sg

a = ['非常满意', '满意', '一般','不满意']
layout = [
    [sg.T('1.'+ a[0]),],
    [sg.R(i,group_id=1)for i in a],
    [sg.T('2.'+ a[1]),],
    [sg.R(i,group_id=2)for i in a],
    [sg.T('3.'+ a[2]),],
    [sg.R(i,group_id=3)for i in a],
    [sg.T('4.'+ a[3]),],
    [sg.R(i,group_id=4)for i in a]
]



window = sg.Window('AC_FUN', layout)
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break
