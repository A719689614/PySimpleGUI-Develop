import PySimpleGUI as sg 
layout_1 = [
    [sg.T('Account'),sg.In(size=(46,0))],
    [sg.T('Password'),sg.In()],
    [sg.B('Confirm'),sg.B('Cancel')]
    ]
list=['one','two','three','four']
layout_2 = [
    [sg.LB(list,size=(0,4))]
]
layout= [
    [sg.Frame(title='Security',layout=layout_1,key='-LY1-'),
     sg.Frame(title='Security',layout=layout_2,key='-LY2-')]

    
]

window = sg.Window('AC_FUN',layout)
while True:
    event,values = window.read()
    if event == None:
        break
    if event == 'Confirm':
        window['-LY1-'].update(visible=False)
window.close()