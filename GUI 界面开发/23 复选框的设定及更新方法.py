# syntax
# sg.Checkbox()or sg.CB()
# 更新方法
# window[key].update()
import PySimpleGUI as sg 
event = None
values = None

# layout = [
#     [sg.CB('1')],
#     [sg.CB('2')],
#     [sg.CB('3')],
#     [sg.CB('4')],
#     ]

layout_1 = [
    [sg.CB(i) for i in range(10)],]
layout_2 = [
    [sg.CB(i)] for i in range(10)],

window = sg.Window('AC_FUN', layout=layout_2)
while True:
    event, values =window.read()
    if event is None:
        break



window.close()