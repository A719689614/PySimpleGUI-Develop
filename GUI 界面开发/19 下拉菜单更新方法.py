import PySimpleGUI as sg

dict = {'程序员1':'python','程序员2':'java','程序员3':'php','程序员4':'c++'}

list = []
for key in dict:
    # print(key)
    list.append(key)

layout = [
    [sg.Combo(list,key='-LB-',size=(30,10),enable_events=True,font=('黑体',10))],
    [sg.T('language'),sg.In(size=20,key='-In-')]
]

window = sg.Window('AC_FUN', layout)
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break
    if event == '-LB-':
        window['-In-'].update(dict[values['-LB-']])